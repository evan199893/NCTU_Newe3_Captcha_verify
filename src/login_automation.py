"""Preferred entry point for Selenium automation."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    runpy.run_path(str(ROOT / "login_automation.py"), run_name="__main__")
