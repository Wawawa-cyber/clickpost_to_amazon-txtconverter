Place encoding-japanese library here to enable reliable Shift_JIS encode/decode in the browser.

Recommended file names:
- encoding.min.js (preferred)
- encoding.js (fallback)

Project: https://github.com/polygonplanet/encoding.js
Usage in this repo:
- build index.html via: python tools/build_web_index.py (or build-web-index.bat)
- Open index.html. The page will automatically load vendor/encoding.min.js (or encoding.js) if present.
- Without this library, the page falls back to TextDecoder/TextEncoder, which may output UTF-8 depending on the browser.

