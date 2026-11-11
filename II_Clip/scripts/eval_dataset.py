# scripts/eval_dataset.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from config import SEASON_DIR
from prompts import SEASON_PROMPTS
from model import encode_text_prompts
from evaluate import evaluate_on_folders

if __name__ == "__main__":
    names, feats = encode_text_prompts(SEASON_PROMPTS)
    evaluate_on_folders(SEASON_DIR, names, feats)