# Publishing a preview release

The public ZIP and website are versioned separately from the experimental implementation handoff. Keep prior tags and ZIPs unchanged.

1. Update `bootstrap.json`, `BOOTSTRAP.md`, the platform guides, website links, and any pinned extension link to the new release tag. Give the new ZIP a release-specific filename in `scripts/build_preview_zip.py` and the package check.
2. Build the ZIP with `python3 scripts/build_preview_zip.py`. Calculate its SHA-256 digest and update `dist/SHA256SUMS.txt` and the two digest values in `dist/install.html`. The checksum file stays outside the ZIP to avoid a self-referential hash.
3. Open a pull request. Wait for the required validation and security checks, then merge. Use the **merged commit**, not the pre-merge branch commit, for the release tag.
4. Create and push an annotated **SSH-signed** tag for that merged commit. Confirm the tag shows **Verified** on GitHub. Do not move a published version tag. Wait for the `Preview build provenance` workflow on that tag to pass. It rebuilds the ZIP, compares it with the committed bytes and checksum, and attests the resulting artifact. A manual workflow run is useful for checking the workflow, but its attestation names the branch commit, not the release tag.
5. Create a **draft** GitHub Release for the tag, attach the exact ZIP and `SHA256SUMS.txt`, and publish the draft. Repository release immutability applies at publication, so attach everything before publishing. Verify the published Release and its downloaded asset with GitHub CLI and the checksum file. Verify build provenance for the downloaded ZIP with `gh attestation verify PATH/TO/ZIP --repo brewser123/business-before-agents --source-ref refs/tags/TAG --signer-workflow brewser123/business-before-agents/.github/workflows/preview-build-provenance.yml`, replacing the path and tag. The verified source commit should match the signed tag's target.
6. Publish the matching merged source to the public website. Check the live ZIP against the Release asset, test the browser checker, and verify setup links point to the new tag.

Review [HOSTING_SECURITY.md](HOSTING_SECURITY.md) before changing the website host or claiming HTTP response-header coverage.

An immutable-release attestation proves which tag and assets GitHub published. The separate build-provenance attestation proves that the same ZIP bytes were rebuilt in the tagged GitHub Actions workflow. Both checks are required before calling a new release build-attested.
