"""Guard against accidental publication of private files or stale downloads."""

import json
import hashlib
import stat
import unittest
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
ARCHIVE = DIST / "business-before-agents-v0.1-preview.zip"
PREFIX = "business-before-agents-v0.1-preview/"
PACKAGE_EXTRAS = {
    "ATTRIBUTION.md", "BOOTSTRAP.md", "LICENSE", "SECURITY.md",
    "LICENSES/CC-BY-4.0.txt", "LICENSES/MIT.txt", "bootstrap.json",
    "platforms/chatgpt/GITHUB_GUIDED_SETUP.md",
    "platforms/chatgpt/PROJECT_SETUP.md",
    "platforms/claude/GITHUB_GUIDED_SETUP.md",
    "platforms/claude/PROJECT_SETUP.md",
    "platforms/local-ai/OPENWEBUI_SETUP.md",
}


class PageAssets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.csp = None
        self.scripts = []
        self.stylesheets = []
        self.inline_handlers = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "content-security-policy":
            self.csp = attrs.get("content")
        if tag == "script":
            self.scripts.append(attrs.get("src"))
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs.get("href"))
        self.inline_handlers.extend(key for key in attrs if key.startswith("on"))


class PublicPackageTests(unittest.TestCase):
    def test_download_checksum_matches_archive_and_checker(self):
        digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
        expected = (DIST / "SHA256SUMS.txt").read_text().strip()
        self.assertEqual(expected, f"{digest}  {ARCHIVE.name}")
        self.assertIn(f'data-sha256="{digest}"', (DIST / "install.html").read_text())

    def test_guided_setup_points_to_the_packaged_release(self):
        manifest = json.loads((ROOT / "bootstrap.json").read_text())
        release = manifest["release"]
        self.assertIn(f"Release: **{release}**", (ROOT / "BOOTSTRAP.md").read_text())
        install = (DIST / "install.html").read_text()
        for path in (
            "BOOTSTRAP.md",
            "platforms/chatgpt/GITHUB_GUIDED_SETUP.md",
            "platforms/claude/GITHUB_GUIDED_SETUP.md",
        ):
            self.assertIn(f"/blob/{release}/{path}", install)

    def test_archive_contains_only_current_public_files(self):
        manifest = json.loads((ROOT / "bootstrap.json").read_text())
        allowed = set(manifest["required_files"]) | set(manifest["optional_files"]) | PACKAGE_EXTRAS
        with ZipFile(ARCHIVE) as archive:
            self.assertIsNone(archive.testzip())
            names = [info.filename for info in archive.infolist()]
            self.assertEqual(len(names), len(set(names)), "Duplicate ZIP entry")
            files = set()
            for info in archive.infolist():
                name = info.filename
                self.assertTrue(name.startswith(PREFIX), name)
                relative = name[len(PREFIX):]
                self.assertNotIn("\\", relative, name)
                parts = PurePosixPath(relative).parts
                self.assertNotIn("..", parts, name)
                if info.is_dir():
                    continue
                self.assertTrue(parts, name)
                self.assertIn(relative, allowed, name)
                self.assertNotEqual((info.external_attr >> 16) & 0o170000, stat.S_IFLNK, name)
                source = ROOT.joinpath(*parts)
                self.assertTrue(source.is_file(), name)
                self.assertEqual(archive.read(name), source.read_bytes(), f"Stale archive file: {name}")
                files.add(relative)
            self.assertEqual(files, allowed)

    def test_static_pages_use_local_assets_and_restrictive_csp(self):
        pages = list(DIST.glob("*.html"))
        self.assertTrue(pages)
        header_rules = (DIST / "_headers").read_text()
        header_policy = header_rules.split("Content-Security-Policy: ", 1)[1].splitlines()[0]
        self.assertIn("X-Content-Type-Options: nosniff", header_rules)
        for page in pages:
            with self.subTest(page=page.name):
                parsed = PageAssets()
                parsed.feed(page.read_text())
                self.assertIsNotNone(parsed.csp)
                self.assertEqual(parsed.csp, header_policy)
                self.assertIn("default-src 'none'", parsed.csp)
                self.assertIn("script-src 'self'", parsed.csp)
                self.assertIn("object-src 'none'", parsed.csp)
                self.assertNotIn("unsafe-inline", parsed.csp)
                self.assertNotIn("unsafe-eval", parsed.csp)
                self.assertFalse(parsed.inline_handlers)
                for asset in parsed.scripts + parsed.stylesheets:
                    self.assertIsNotNone(asset, "Inline script is not allowed")
                    self.assertFalse(asset.startswith(("http:", "https:", "//", "/")), asset)
                    self.assertTrue((DIST / asset).is_file(), asset)


if __name__ == "__main__":
    unittest.main()
