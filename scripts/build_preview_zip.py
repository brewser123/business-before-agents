"""Build the public framework archive from an explicit file allowlist."""

import json
import os
import stat
import tempfile
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "dist/business-before-agents-v0.1-preview.zip"
PREFIX = "business-before-agents-v0.1-preview/"
EXTRAS = {
    "ATTRIBUTION.md", "BOOTSTRAP.md", "LICENSE", "SECURITY.md",
    "LICENSES/CC-BY-4.0.txt", "LICENSES/MIT.txt", "bootstrap.json",
    "platforms/chatgpt/GITHUB_GUIDED_SETUP.md",
    "platforms/chatgpt/PROJECT_SETUP.md",
    "platforms/claude/GITHUB_GUIDED_SETUP.md",
    "platforms/claude/PROJECT_SETUP.md",
    "platforms/local-ai/OPENWEBUI_SETUP.md",
}


def main():
    manifest = json.loads((ROOT / "bootstrap.json").read_text())
    public_files = sorted(set(manifest["required_files"]) | set(manifest["optional_files"]) | EXTRAS)
    fd, temporary = tempfile.mkstemp(suffix=".zip", dir=ARCHIVE.parent)
    os.close(fd)
    try:
        with ZipFile(temporary, "w") as archive:
            for relative in public_files:
                path = PurePosixPath(relative)
                if path.is_absolute() or ".." in path.parts or "\\" in relative or str(path) != relative:
                    raise ValueError(f"Unsafe archive path: {relative}")
                source = ROOT / relative
                if not source.is_file() or source.is_symlink():
                    raise ValueError(f"Missing or unsafe public file: {relative}")
                entry = ZipInfo(PREFIX + relative, date_time=(2024, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = (stat.S_IFREG | 0o644) << 16
                archive.writestr(entry, source.read_bytes())
        with ZipFile(temporary) as check:
            if check.testzip() is not None:
                raise ValueError("Public archive failed integrity check")
        os.replace(temporary, ARCHIVE)
        print(f"Built {ARCHIVE.name} from {len(public_files)} public files")
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


if __name__ == "__main__":
    main()
