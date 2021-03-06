## `py-qmoji`
A python script that converts strings to QR Code built using Emojis. The output can be copied & pasted into messaging apps and then scanned using a QR Code reader

```
⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬜⬜⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛
⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬛⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬜⬛⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬛
⬛⬜⬛⬛⬜⬜⬜⬛⬜⬛⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜
⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛⬛
⬜⬜⬜⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜
⬛⬜⬛⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬛⬛⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬛⬜⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬛⬛⬜⬛⬜
⬛⬜⬛⬛⬛⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜
```

## Why? 
So I can annoy my friends with QR codes on social media.

## What?
Runs on `python 2.7.x`.

Requires `qrcode`, `numpy`, and `emoji`.

Install packages individually using `pip install [packagename]`

## How?
Edit `main.py` line 29 to change your input. Execute using `python main.py`. Open `output.txt` for your qmoji. If you need to add a border, simply change line 24 to do so.

## Testing?
So far I've tested the output on the following apps, exclusively using the desktop/web-browser since phone screens cannot properly display emojis that are at least 21 characters wide. All the following have been tested using a borderless qmoji (21x21) at minimum, and then gradually increased to find the maximum. Bordered qmoji's have minumum size of 23x23 respectively.

| Application   | Pastes correctly | Scannable by QR Code Scanner | Max qmoji size  | Notes |
| :--           | :---:            | :---:                        | :---:           |:---  |
| Whatsapp Web  | ✔️               | ✔️                          | 21 x 21        | no border | 
| Mattermost    | ✔️               | ✔️                          | 35 x 35        | border, dark theme |
| Discord       | ✔️(line by line) | ✔️                          | 23 x 23        | border, dark theme |
| Telegram Web  | ✖️               | ✖️                          | n/a            | |
| Twitter       | ✖️               | ✖️                          | n/a            | |
| TwitLonger    | ✔️               | ✖️                          | n/a            | |
| Steam         | ✔️               | ✔️                          | 35 x 35        | border, dark theme |
| Git Markdown  | ✔️               | ✖️                          | n/a            | inside code block |
| Facebook Post | ✔️               | ✔️                         | 21 x 21         | no border |
| Reddit Post   | ✔️ (quotation)  | ✔️                         | 21 x 21         | border, dark theme |
| Tumblr Post   | ✔️              | ✖️                          | n/a            | |

Tested using [QR Code Scanner](https://play.google.com/store/apps/details?id=tw.mobileapp.qrcode.banner&hl=en) on a Huawei P9-Lite.

## Findings?
There are three clear limitations to using `qmoji` on social media. These are:

* Character line width 
* Max character length
* Dark background theme

The prodominant factor is the character line width -- since exceeding it causes the text to wrap onto a new line; there is no clear solution to avoid this. Certain apps have a message character length, specifically Twitter and Discord, but can be mitigated at times by pasting the qmoji line by line. Surprisingly, dark theme apps work *very well* with more room for error but requires a white border around the qmoji, thereby increasing its overall size. 

Overall it comes down to how the emojis are visually represented on the platform, miscellaneous factors such as font style, character seperations, and zoom scaling can all play a part in how the qmoji is  displayed and read.

## TODO?

* Proper CMD input/output
* Dynamic emoji selection
* Better output (no more opening a generated file)
* 8bit emoji art generator?
