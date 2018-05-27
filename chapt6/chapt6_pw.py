#! python3
# pw.py - pw manager, Vulnerable

import sys
import pyperclip

PASSWORDS = {"email" : "aaaaa", "pc" : "bbbbbb", "amazon" : "cccccc"}

if len(sys.argv) < 2:
    print("How to use:python pw.py [Account name]")
    print("Copy the pw to clip board.")
    sys.exit()

account = sys.argv[1]#Command line 2nd argument is the account name.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("The pass word of " + account + " was successfully copied.")
else:
    print(account + "not exsist.")