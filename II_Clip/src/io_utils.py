# src/io_utils.py
import csv
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

def list_images(folder):
    return sorted(p for p in Path(folder).iterdir() if p.suffix.lower() in IMAGE_EXTS)

def write_csv(rows, csv_path):
    if not rows:
        return
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)