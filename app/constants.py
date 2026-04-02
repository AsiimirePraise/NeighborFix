"""Display labels and hero imagery for category slugs (Unsplash, editorial use)."""

# Hero images on report detail — greyscale applied in CSS for brand consistency
CATEGORY_IMAGE_URLS: dict[str, str] = {
    "streets": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=80&auto=format&fit=crop",
    "lighting": "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&q=80&auto=format&fit=crop",
    "sanitation": "https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=1600&q=80&auto=format&fit=crop",
    "safety": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1600&q=80&auto=format&fit=crop",
    "parks": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&q=80&auto=format&fit=crop",
    "water": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=1600&q=80&auto=format&fit=crop",
    "traffic": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1600&q=80&auto=format&fit=crop",
    "other": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1f?w=1600&q=80&auto=format&fit=crop",
}

CATEGORY_LABELS: dict[str, str] = {
    "streets": "Streets & sidewalks",
    "lighting": "Lighting",
    "sanitation": "Sanitation",
    "safety": "Safety & noise",
    "parks": "Parks & trees",
    "water": "Water & drainage",
    "traffic": "Traffic & signs",
    "other": "Other",
}
