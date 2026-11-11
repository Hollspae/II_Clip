# src/evaluate.py
from collections import defaultdict
from pathlib import Path
from PIL import Image
from classify import classify_image
from io_utils import IMAGE_EXTS

def evaluate_on_folders(root, class_names, text_features):
    correct, total = 0, 0
    confusion = defaultdict(lambda: defaultdict(int))
    for true_class in class_names:
        class_dir = Path(root) / true_class
        if not class_dir.is_dir():
            continue
        for path in class_dir.iterdir():
            if path.suffix.lower() not in IMAGE_EXTS:
                continue
            try:
                pred = classify_image(Image.open(path).convert("RGB"),
                                      class_names, text_features, topk=1)[0][0]
            except Exception:
                continue
            confusion[true_class][pred] += 1
            total += 1
            correct += int(pred == true_class)
    if total == 0:
        print("Размеченных папок не найдено.")
        return
    print(f"\nAccuracy: {correct/total*100:.2f}%  ({correct}/{total})")
    print("              " + " ".join(f"{c:>10s}" for c in class_names))
    for t in class_names:
        print(f"{t:>12s}: " + " ".join(f"{confusion[t][p]:>10d}" for p in class_names))