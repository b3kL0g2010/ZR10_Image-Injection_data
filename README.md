# ZR10 Image Metadata Injection (PX4 Photogrammetry)

This repository contains a Python-based pipeline for injecting **GPS coordinates and UTC timestamps** into **ZR10 / SIYI images** using **PX4 ULog flight data**.  
It is intended for **photogrammetry and mapping missions** where captured images do not contain EXIF metadata.

📺 **Video Walkthrough**  
A complete execution demo is available here:  
https://youtu.be/sminpPicBdA

---

## Features

- Extracts GPS and attitude data from PX4 `.ulg` logs  
- Converts PX4 timestamps to UTC  
- Samples metadata at a configurable time interval  
- Assigns metadata to images without modifying originals  
- Injects GPS and Date/Time EXIF data using `exiftool`  
- Supports full pipeline automation  

---

## Project Structure

```
Tanay_01-14-26/
│
├── log_27_2026-1-13-11-15-06.ulg   # PX4 flight log
├── 101SIYI_IMG/                  # Original images (untouched)
├── 101SIYI_IMG_GEO/              # Output images (with metadata)
│
├── extract_ulog.py               # Extract GPS & attitude from ULog
├── gps_utc.py                    # Convert PX4 time to UTC
├── sample_every_3s.py            # Sample metadata (time-based)
├── assign_images.py              # Match images to metadata
├── write_exif.py                 # Inject EXIF data
├── run_pipeline.py               # Full automation script
│
├── gps.csv
├── gps_utc.csv
├── attitude.csv
├── sampled_metadata.csv
├── image_metadata.csv
│
└── temp/                         # Python virtual environment
```

---

## Prerequisites

### Operating System
- Ubuntu (tested)

### System Packages
```bash
sudo apt update
sudo apt install -y python3-pip python3.12-venv exiftool
```

### Python
- Python 3.12
- Virtual environment required

### Python Packages
Install **inside the virtual environment**:
```bash
python -m pip install --upgrade pip
python -m pip install pyulog pandas numpy pytz
```

---

## Virtual Environment Setup

```bash
python3 -m venv temp
source temp/bin/activate
```

Ensure the environment is activated before running any script.

---

## Manual Execution (Step-by-Step)

Run the scripts **in the following order**.

### 1. Extract PX4 ULog Data
```bash
python extract_ulog.py
```
Outputs:
- `gps.csv`
- `attitude.csv`

---

### 2. Convert GPS Time to UTC
```bash
python gps_utc.py
```
Output:
- `gps_utc.csv`

---

### 3. Sample Metadata
```bash
python sample_every_3s.py
```
Modify the sampling interval inside the script as needed.

Output:
- `sampled_metadata.csv`

---

### 4. Assign Metadata to Images
```bash
python assign_images.py
```

- Creates `101SIYI_IMG_GEO/`
- Original images remain untouched

Output:
- `101SIYI_IMG_GEO/image_metadata.csv`

---

### 5. Inject EXIF Metadata
```bash
python write_exif.py
```

Result:
- `101SIYI_IMG_GEO/*.JPG`  
Images now contain GPS coordinates and Date/Time metadata.

---

## Automated Pipeline (Recommended)

Once the output image folder exists:

```bash
python run_pipeline.py
```

Requirements:
- Must be inside the Python virtual environment
- Wait for the script to fully finish before checking results

This executes all five steps automatically.

---

## Verify Metadata Injection

```bash
exiftool 101SIYI_IMG_GEO/$(ls 101SIYI_IMG_GEO | head -n 1)
```

Confirm the presence of:
- `GPSLatitude`
- `GPSLongitude`
- `DateTimeOriginal`

---

## Notes

- Designed for PX4-based UAVs  
- Tested with ZR10 / SIYI image sets  
- Suitable for mapping, surveying, and academic research  

---

## License

MIT License

Copyright © 2026 JPD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
