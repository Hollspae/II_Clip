# src/config.py
from pathlib import Path
import torch

ROOT = Path(__file__).resolve().parent.parent

MODEL_NAME = "ViT-B/32"

SEASON_DIR = ROOT / "data" / "season"
AERIAL_DIR = ROOT / "data" / "aerial"

AERIAL_ALL_DIR = ROOT / "data" / "aerial_all" 

OUTPUT_DIR = ROOT / "outputs"
CSV_DIR    = OUTPUT_DIR / "csv"
CSV_DIR.mkdir(parents=True, exist_ok=True)

TOPK = 3
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"