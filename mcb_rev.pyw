#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存 ❶
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open("mcb")

if len(sys.argv) == 3:
    if sys.argv[1].lower == "save":
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower == "delete":
        mcb_shelf[sys.argv[2]] = ""

elif len(sys.argv) == 2:
    if sys.argv[1].lower == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    
    elif sys.argv[1].lower == "delete":
        for i in list(mcb_shelf.keys()):
            mcb_shelf[i] = ""
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
