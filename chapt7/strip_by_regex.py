import re

def stripbregx(sent, word):

    if re.compile(r"^\s*").search(sent) != None and\
    re.compile(r"\s*$").search(sent) != None:
        res = re.compile(r"^\s*").sub("", sent)
        res = re.compile(r"\s*$").sub("", res)
    
    else:
        wordsb = "^" + word 
        wordse = word + "$"
        res = re.compile(wordsb).sub("", sent)
        res = re.compile(wordse).sub("", res)

    return res

sent = input("Input sentence:")
word = input("Input words to remove:")

result = stripbregx(sent, word)
print(result)