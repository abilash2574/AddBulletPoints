#! python3
# AddBulletPoints.py -- use this to add bullet points to the list of text copied
# to the clipboard and it copies the new text to clipboard.

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

print(text)

pyperclip.copy(text)
