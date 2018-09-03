import pyperclip
import time

ls = []

while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()
        if value not in ls:
            ls.append(value)
        print ls
        time.sleep(3)

