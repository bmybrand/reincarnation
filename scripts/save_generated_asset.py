from pathlib import Path
import sys

from PIL import Image


if len(sys.argv) != 3:
    raise SystemExit("Usage: save_generated_asset.py SOURCE DESTINATION")

source = Path(sys.argv[1])
destination = Path(sys.argv[2])
destination.parent.mkdir(parents=True, exist_ok=True)

with Image.open(source) as image:
    image.convert("RGB").save(destination, "WEBP", quality=88, method=6)

print(destination)
