#! python3
# bulletPointAdder.py - add points on the top of
# sentence in clip borad.

import pyperclip

text = pyperclip.paste()
lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = "*" + lines[i]

text = "\n".join(lines)

pyperclip.copy(text)