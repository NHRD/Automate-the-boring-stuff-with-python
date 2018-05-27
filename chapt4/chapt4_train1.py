spam = ["a", "b", "c", "d", "e"]

for c in range(len(spam)):
    if c < len(spam) - 1:
        print(spam[c] ,end = ", ")
    else:
        print("and " + spam[c] +  ".")
