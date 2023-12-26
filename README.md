# QR-Code-Wallpaper
This Python script generates a QR code and overlays it onto a background image. The resulting image can be used as a custom wallpaper to easily share links at networking events.

The background was made using Adobe Express.

First run `qr_code_generator.py` to create the qr code.

Then run `qr_code_overlay.py` to add the newly created qr code to the background.

## Prerequisites
- Python 3.x
- Install required libraries:

  ```bash
  pip install qrcode

## Customization
Adjust the QR code parameters in `qr_code_generator.py`:
- box_size: Size of the QR code box.
- border: Border around the QR code.

Adjust the QR code position in `qr_code_overlay.py`:
- overlay_position: Position the QR code on the background image.

