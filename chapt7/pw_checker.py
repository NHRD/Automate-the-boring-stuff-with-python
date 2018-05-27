import re

def pw_strength(pw):
    if len(pw) < 8:
        print("Weak pw.")
    elif re.compile(r"[A-Z]").search(pw) == None or\
     re.compile(r"[a-z]").search(pw) == None or\
      re.compile(r"\d").search(pw) == None:
        print("Weak pw.")
    
    else:
        print("Strong pw.")

pw = input("Input pw to be checked.:")
pw_strength(pw)