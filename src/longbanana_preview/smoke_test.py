"""Small test module for the anonymous LongBanana review scaffold."""

from __future__ import annotations

import hashlib


def preview_checksum(text: str = "longbanana-review") -> str:
    """Return a short deterministic checksum for smoke testing imports."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def smoke_status() -> str:
    return f"LongBanana smoke test passed: {preview_checksum()}"


if __name__ == "__main__":
    print(smoke_status())
