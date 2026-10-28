from pathlib import Path
import json

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets" / "generated" / "image-manifest.json"

mapping = json.loads(MANIFEST.read_text(encoding="utf-8"))["images"]
sources = {
    ROOT
    / generated.replace("-tiles-v2.webp", ".webp")
    .replace("-tiles.webp", ".webp")
    .lstrip("/")
    for generated in mapping.values()
    if not generated.endswith("homepage-digital-intelligence.webp")
}

canvas_size = (1024, 768)
panels = (
    (34, 0, 990, 195),
    (0, 213, 1024, 555),
    (34, 573, 990, 768),
)

created = 0
for source in sorted(sources):
    destination = source.with_name(f"{source.stem}-tiles-v2.webp")

    with Image.open(source) as image:
        fitted = ImageOps.fit(
            image.convert("RGBA"), canvas_size, method=Image.Resampling.LANCZOS
        )

    result = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    for left, top, right, bottom in panels:
        tile = fitted.crop((left, top, right, bottom))
        mask = Image.new("L", tile.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            (0, 0, tile.width - 1, tile.height - 1), radius=13, fill=255
        )
        result.paste(tile, (left, top), mask)

    result.save(destination, "WEBP", quality=90, method=6)
    created += 1
    print(destination.relative_to(ROOT))

print(f"Created {created} three-tile variants.")
