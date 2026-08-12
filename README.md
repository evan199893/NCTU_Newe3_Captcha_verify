# NCTU/NYCU e3 CAPTCHA Verify (CNN + Selenium)

This repository contains a full pipeline to solve 4-digit CAPTCHA images used by the e3 login page:

1. Collect CAPTCHA images
2. Clean and split digits
3. Train a CNN classifier
4. Predict CAPTCHA text
5. Auto-fill and submit login form with Selenium

Demo video: https://youtu.be/KA4EvdrpzaM

## Project Structure

- `scrape.py`: download many CAPTCHA images for dataset collection
- `tt3.py`: background noise reduction and crop normalization (stage 1)
- `tt44.py`: digit boundary detection and splitting (stage 2)
- `tt55.py`: width normalization to fixed input size (stage 3)
- `train.py`: train CNN model and save model file
- `predict.py`: predict 4-digit CAPTCHA from an image
- `split_digits_in_img.py`: reusable digit segmentation helper used by Selenium flow
- `selepublic.py`: single-thread Selenium login automation with CAPTCHA solving
- `selepublic_v2.py`: multi-thread variant (model load + browser flow)
- `cnn_model.h5`: pre-trained model artifact

## Requirements

Use Python 3.8+ (recommended). Install dependencies:

```bash
pip install numpy requests pillow opencv-python matplotlib scikit-learn tensorflow selenium
```

Also install:

- Google Chrome
- Matching ChromeDriver version

## Quick Start (Use Pretrained Model)

If you only want login automation with the provided model:

1. Keep `selepublic.py`, `split_digits_in_img.py`, and `cnn_model.h5` in the same folder.
2. Update your credentials in `selepublic.py`.
3. Ensure Selenium can launch Chrome (ChromeDriver configured in PATH or script).
4. Run:

```bash
python selepublic.py
```

## Full Training Pipeline

### 1) Collect CAPTCHA images

```bash
python scrape.py
```

Default behavior downloads images into `./photo/`.

### 2) Preprocess dataset

Run the scripts in this order:

1. `tt3.py` (denoise and align)
2. `tt44.py` (split each CAPTCHA into digits)
3. `tt55.py` (normalize each digit image width)

Before running, update path placeholders in these files so input/output folders match your local machine.

### 3) Prepare labeled training folder

`train.py` expects digit images in `traning1/` (repository keeps original folder name). Labels are read from file names (the character right before `.png`).

### 4) Train model

```bash
python train.py
```

The script trains a CNN and saves an `.h5` model.

## CAPTCHA Prediction

Use `predict.py` to test a CAPTCHA image:

```bash
python predict.py
```

When prompted, provide a CAPTCHA image path. The script segments 4 digits and prints per-digit prediction/confidence.

## Selenium Login Automation

### `selepublic.py`

- Opens e3 login page
- Captures CAPTCHA image from page
- Uses CNN model to predict 4-digit code
- Fills username, password, and CAPTCHA
- Submits login form

Edit credentials before running.

### `selepublic_v2.py`

Alternative implementation using multithreading to overlap model loading and browser interaction.

## Important Notes

- Several scripts contain hard-coded absolute paths from the original development environment. Update these paths before use.
- Some code uses legacy TensorFlow/Keras APIs (for example `predict_classes`). For modern TensorFlow versions, you may need to replace this with `np.argmax(model.predict(...), axis=1)`.
- `selepublic_v2.py` sets a hard-coded ChromeDriver path. Update it for your system.
- CAPTCHA and login page HTML can change over time. XPath or ID selectors may need maintenance.

## Troubleshooting

- Model not found:
	- Ensure `cnn_model.h5` is in the current working directory.
- Selenium cannot start Chrome:
	- Verify ChromeDriver version matches installed Chrome.
	- Confirm ChromeDriver is executable and discoverable.
- Prediction quality is poor:
	- Rebuild dataset and retrain model.
	- Validate preprocessing output from `tt3.py` -> `tt44.py` -> `tt55.py`.

## License

This project is released under the terms in `LICENSE`.
