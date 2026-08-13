"""Preferred entry point for model training."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "train_cnn.py"), run_name="__main__")
