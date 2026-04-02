"""One-off: download hero images into app/static/img (run from repo root)."""
from __future__ import annotations

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "app" / "static" / "img"
CAT = IMG / "categories"

# Same sources as before — stored locally for reliable deploy (no hotlink 403s).
URLS: dict[str, str] = {
    "home-bg.jpg": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1f?w=1920&q=80&auto=format&fit=crop",
    "categories/streets.jpg": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=75&auto=format&fit=crop",
    "categories/lighting.jpg": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&q=75&auto=format&fit=crop",
    "categories/sanitation.jpg": "https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=1600&q=75&auto=format&fit=crop",
    "categories/safety.jpg": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1600&q=75&auto=format&fit=crop",
    "categories/parks.jpg": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&q=75&auto=format&fit=crop",
    "categories/water.jpg": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=1600&q=75&auto=format&fit=crop",
    "categories/traffic.jpg": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1600&q=75&auto=format&fit=crop",
    "categories/other.jpg": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1f?w=1600&q=75&auto=format&fit=crop",
}


def main() -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    CAT.mkdir(parents=True, exist_ok=True)
    for rel, url in URLS.items():
        dest = IMG / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("fetch", url[:60], "->", dest.relative_to(ROOT))
        urllib.request.urlretrieve(url, dest)
    print("done.")


if __name__ == "__main__":
    main()
