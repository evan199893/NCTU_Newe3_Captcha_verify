"""Preferred entry point for stage 1 preprocessing."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "preprocess_stage_1_denoise.py"), run_name="__main__")
