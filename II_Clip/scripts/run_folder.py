# scripts/run_folder.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from main import run_task
from config import SEASON_DIR, AERIAL_DIR
from prompts import SEASON_PROMPTS, AERIAL_PROMPTS

if __name__ == "__main__":
    run_task("Время года (аэро)", SEASON_DIR, SEASON_PROMPTS, "season_results.csv")
    run_task("Ландшафт с неба", AERIAL_DIR, AERIAL_PROMPTS, "aerial_results.csv")