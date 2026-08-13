"""Preferred entry point for single-image CAPTCHA prediction."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "predict_captcha.py"), run_name="__main__")
