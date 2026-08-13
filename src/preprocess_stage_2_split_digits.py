"""Preferred entry point for stage 2 preprocessing."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "preprocess_stage_2_split_digits.py"), run_name="__main__")
