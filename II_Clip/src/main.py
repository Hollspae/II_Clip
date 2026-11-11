import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import SEASON_DIR, AERIAL_DIR, AERIAL_ALL_DIR, CSV_DIR
from prompts import SEASON_PROMPTS, AERIAL_PROMPTS
from model import encode_text_prompts
from classify import classify_image
from io_utils import list_images, write_csv

def run_task(name, folder, prompts, csv_name):
    class_names, text_features = encode_text_prompts(prompts)
    files = list_images(folder)
    print(f"\n=== {name}: {len(files)} файлов ===")
    rows = []
    for path in files:
        try:
            results = classify_image(Image.open(path).convert("RGB"),
                                     class_names, text_features)
        except Exception as e:
            print(f"{path.name:30s} -> ОШИБКА: {e}")
            continue
        line = " | ".join(f"{c}: {p*100:.1f}%" for c, p in results)
        print(f"{path.name:30s} -> {line}")
        rows.append({"file": path.name,
                     "top1": results[0][0], "top1_prob": round(results[0][1], 4),
                     "top2": results[1][0], "top2_prob": round(results[1][1], 4),
                     "top3": results[2][0], "top3_prob": round(results[2][1], 4)})
    write_csv(rows, CSV_DIR / csv_name)

if __name__ == "__main__":
    run_task("Время года (аэро)", AERIAL_ALL_DIR, SEASON_PROMPTS, "season_results.csv")
    run_task("Ландшафт с неба",   AERIAL_ALL_DIR, AERIAL_PROMPTS, "aerial_results.csv")