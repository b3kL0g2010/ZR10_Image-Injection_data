import pandas as pd
import subprocess
from pathlib import Path

IMG_DIR = Path("101SIYI_IMG_GEO")
CSV = "image_metadata.csv"

df = pd.read_csv(CSV)

for _, r in df.iterrows():
    img_path = IMG_DIR / r["image"]

    # UTC → EXIF format
    utc = pd.to_datetime(r["utc"])
    exif_time = utc.strftime("%Y:%m:%d %H:%M:%S")

    cmd = [
        "exiftool",
        "-overwrite_original",
        f"-GPSLatitude={r['lat']}",
        f"-GPSLongitude={r['lon']}",
        f"-GPSAltitude={r['alt_msl']}",
        "-GPSLatitudeRef=N",
        "-GPSLongitudeRef=E",
        f"-DateTimeOriginal={exif_time}",
        f"-CreateDate={exif_time}",
        str(img_path)
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("✔ EXIF GPS + UTC written to images")
