import pandas as pd
from pathlib import Path
import shutil

SRC_DIR = Path("101SIYI_IMG")
DST_DIR = Path("101SIYI_IMG_GEO")

DST_DIR.mkdir(exist_ok=True)

df = pd.read_csv("sampled_metadata.csv")

images = sorted(
    list(SRC_DIR.glob("*.jpg")) +
    list(SRC_DIR.glob("*.JPG")) +
    list(SRC_DIR.glob("*.jpeg")) +
    list(SRC_DIR.glob("*.JPEG"))
)

print(f"Found {len(images)} images")

usable = min(len(images), len(df))

df = df.iloc[:usable].copy()

new_names = []
for img in images[:usable]:
    shutil.copy2(img, DST_DIR / img.name)
    new_names.append(img.name)

df["image"] = new_names

df.to_csv("image_metadata.csv", index=False)

print(f"✔ Copied {usable} images into {DST_DIR}")
