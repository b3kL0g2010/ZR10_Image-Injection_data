import subprocess
import sys

STEPS = [
    ("Extract ULog", "python extract_ulog.py"),
    ("Convert GPS UTC", "python gps_utc.py"),
    ("Sample telemetry (3s)", "python sample_every_3s.py"),
    ("Copy & align images", "python assign_images.py"),
    ("Write EXIF metadata", "python write_exif.py"),
]

def run(step_name, command):
    print(f"\n▶ {step_name}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"\n❌ FAILED at step: {step_name}")
        sys.exit(1)
    print(f"✔ Completed: {step_name}")

if __name__ == "__main__":
    print("=== PX4 → PHOTOGRAMMETRY PIPELINE START ===")

    for name, cmd in STEPS:
        run(name, cmd)

    print("\n=== PIPELINE COMPLETED SUCCESSFULLY ===")
    print("Output images: 101SIYI_IMG_GEO/")
