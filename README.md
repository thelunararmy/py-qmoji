## `py-qmoji`
A python script that converts strings to QR Code built using Emojis. The output can be copied & pasted into messaging apps and then scanned using a QR Code reader

## Why? 
So I can annoy my friends with QR codes on social media.

## What?
Requires `python 2.7.x`.
Requires `qrcode`, `numpy`, and `emoji`.
Install package individually using `pip install [packagename]`

## How?
Edit `main.py` line 29 to change your input. Execute using `python main.py`. Open `output.txt` for your qmoji.

## Testing?
So far I've tested the output on the following apps, exclusively using the desktop/web-browser since phone screens cannot properly display emojis that are at least 21 characters in length.

| Application  | Pastes correctly | Scannable by QR code reader | Max qmoji size |
| :--          | :---:            | :---:                       | :---:          |
| Whatsapp Web | ✓                | ✓                           | 21 x 21       |
