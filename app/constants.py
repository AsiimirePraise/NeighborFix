"""Display labels and static hero assets under app/static/img (works on Render/Railway without hotlinking)."""

# Paths relative to Flask static/ — served as /static/img/...
CATEGORY_IMAGE_FILES: dict[str, str] = {
    "streets": "img/categories/streets.svg",
    "lighting": "img/categories/lighting.svg",
    "sanitation": "img/categories/sanitation.svg",
    "safety": "img/categories/safety.svg",
    "parks": "img/categories/parks.svg",
    "water": "img/categories/water.svg",
    "traffic": "img/categories/traffic.svg",
    "other": "img/categories/other.svg",
}

HOME_BG_FILE = "img/home-bg.svg"

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
