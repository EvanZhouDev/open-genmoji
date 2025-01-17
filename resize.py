from pathlib import Path
from PIL import Image
from typing import Union

def resize_image(input_path: Union[str, Path], scale: int = 5) -> None:
    img = Image.open(input_path)
    output_path = Path(input_path).stem + "-resized" + Path(input_path).suffix
    img.resize((d * scale for d in img.size), Image.LANCZOS).save(output_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        sys.exit("Usage: python resize.py <image_path>")
    resize_image(sys.argv[1])