# Website response-header status

The public website is deployed through Sites as a static site. On November 17, 2026, direct requests for its HTML, CSS, and ZIP files returned no custom `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `Referrer-Policy`, or `Permissions-Policy` response headers. The host served `/_headers` as a downloadable file instead of applying it, so that file was removed.

The HTML pages still contain the restrictive Content Security Policy meta tag. They also set `<meta name="referrer" content="no-referrer">`. These browser-level measures do not replace HTTP response headers, especially for HSTS, MIME sniffing control, permissions policy, or frame embedding controls.

Before claiming full header coverage, use a hosting path that supports response-header configuration, or a carefully tested Worker that sets headers on every response. Preserve all existing static paths, the ZIP download, release checksum, browser checker, and public audience. Verify the deployed response headers on HTML, CSS, and ZIP URLs with an HTTP client. Do not assume a `_headers` file is active just because it is present in a deployment archive.
