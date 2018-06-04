import random, logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("program start.")

#logging.disable(logging.DEBUG)

guess = ""

def top_bottom(face):
    if face == "top":
        return 1
    else:
        return 0

while guess not in ("top", "bottom"):
    logging.debug("guess input starts.")
    print("Input top or bottom")
    guess = input()

guess = top_bottom(guess)

toss = random.randint(0, 1)
if toss == guess:
    logging.debug("if function 1.")
    logging.debug("toss is {}, guess is {}." .format(toss, guess))
    print("YES.")
else:
    logging.debug("if function 2.")
    logging.debug("toss is {}, guess is {}." .format(toss, guess))
    print("No. One more.")
    guess = input()
    guess = top_bottom(guess)
    if toss == guess:
        logging.debug("if function 3.")
        logging.debug("toss is {}, guess is {}." .format(toss, guess))
        print("YES.")
    else:
        logging.debug("if function 4.")
        logging.debug("toss is {}, guess is {}." .format(toss, guess))
        print("No.")

logging.debug("program ends.")
