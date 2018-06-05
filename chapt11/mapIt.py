import sys, webbrowser, pyperclip

address = pyperclip.paste()

webbrowser.open("http://www.google.com/maps/place/" + address)
