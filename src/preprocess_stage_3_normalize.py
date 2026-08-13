"""Preferred entry point for stage 3 preprocessing."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "preprocess_stage_3_normalize.py"), run_name="__main__")
