# NCTU/NYCU e3 CAPTCHA Verify (CNN + Selenium)

This repository contains a full pipeline to solve 4-digit CAPTCHA images used by the e3 login page:

1. Collect CAPTCHA images
2. Clean and split digits
3. Train a CNN classifier
4. Predict CAPTCHA text
5. Automate the login flow with Selenium

Demo video: https://youtu.be/KA4EvdrpzaM

## Project Structure

The repo now uses clearer descriptive names while preserving backward compatibility with the original legacy filenames.

- `collect_captcha_images.py`: downloads CAPTCHA images into a dataset folder
- `preprocess_stage_1_denoise.py`: noise reduction and crop normalization
- `preprocess_stage_2_split_digits.py`: digit boundary detection and splitting
- `preprocess_stage_3_normalize.py`: standardizes digit widths to a fixed input size
- `train_cnn.py`: trains the CNN model and saves the checkpoint
- `predict_captcha.py`: predicts a 4-digit CAPTCHA from a single image
- `digit_segmentation.py`: reusable digit segmentation helper used in automation flows
- `login_automation.py`: single-thread Selenium login automation
- `login_automation_multithreaded.py`: multithreaded alternative that overlaps model loading and browser work
- `cnn_model.h5`: pre-trained model artifact
- `src/`: folder with clearer entry-point wrappers for the same workflow

## Requirements

Use Python 3.8+ (recommended). Install dependencies:

```bash
pip install -r requirements.txt
```

Also install:

- Google Chrome
- Matching ChromeDriver version

## Quick Start (Use Pretrained Model)

If you only want login automation with the provided model:

1. Keep `login_automation.py`, `digit_segmentation.py`, and `cnn_model.h5` in the same folder.
2. Update your credentials in `login_automation.py`.
3. Ensure Selenium can launch Chrome (ChromeDriver configured in PATH or script).
4. Run:

```bash
python login_automation.py
```

## Full Training Pipeline

### 1) Collect CAPTCHA images

```bash
python collect_captcha_images.py
```

Default behavior downloads images into `./photo/`.

### 2) Preprocess dataset

Run the scripts in this order:

1. `preprocess_stage_1_denoise.py` (denoise and align)
2. `preprocess_stage_2_split_digits.py` (split each CAPTCHA into digits)
3. `preprocess_stage_3_normalize.py` (normalize each digit image width)

Before running, update path placeholders in these files so the input/output folders match your local machine.

### 3) Prepare the labeled training folder

`train_cnn.py` expects digit images in `traning1/` (the repository keeps the original folder name). Labels are read from the character immediately before `.png`.

### 4) Train the model

```bash
python train_cnn.py
```

The script trains a CNN and saves an `.h5` model.

## CAPTCHA Prediction

Use `predict_captcha.py` to test a CAPTCHA image:

```bash
python predict_captcha.py
```

When prompted, provide a CAPTCHA image path. The script segments 4 digits and prints per-digit prediction and confidence.

## Selenium Automation

### `login_automation.py`

- Opens the e3 login page
- Captures the CAPTCHA image from the page
- Uses the CNN model to predict the 4-digit code
- Fills username, password, and CAPTCHA
- Submits the login form

Edit your credentials before running.

### `login_automation_multithreaded.py`

Alternative implementation using multithreading to overlap model loading and browser interaction.

## Important Notes

- Several scripts contain hard-coded absolute paths from the original development environment. Update these paths before use.
- Some code uses legacy TensorFlow/Keras APIs (for example `predict_classes`). For modern TensorFlow versions, you may need to replace this with `np.argmax(model.predict(...), axis=1)`.
- `login_automation_multithreaded.py` sets a hard-coded ChromeDriver path. Update it for your system.
- CAPTCHA and login page HTML can change over time. XPath or ID selectors may need maintenance.
- The original legacy names are still accepted as compatibility aliases, but the clearer names above are the preferred ones.

## Troubleshooting

- Model not found:
  - Ensure `cnn_model.h5` is in the current working directory.
- Selenium cannot start Chrome:
  - Verify ChromeDriver version matches the installed Chrome.
  - Confirm ChromeDriver is executable and discoverable.
- Prediction quality is poor:
  - Rebuild the dataset and retrain the model.
  - Validate preprocessing output from `preprocess_stage_1_denoise.py` -> `preprocess_stage_2_split_digits.py` -> `preprocess_stage_3_normalize.py`.

## License

This project is released under the terms in `LICENSE`.
