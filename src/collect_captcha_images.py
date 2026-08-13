"""Preferred entry point for dataset collection."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "collect_captcha_images.py"), run_name="__main__")
