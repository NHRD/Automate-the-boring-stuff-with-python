import re

def sakubun_gen(adj, noun, verb, adv):
    sakubun_file = open(".\\Automate-the-boring-stuff-with-python\\chapt8\\sakubun.txt", "r")
    sakubun = sakubun_file.read()
    sakubun_list = sakubun.split(" ")
    sakubun_out = []
    for i in sakubun_list:
        if re.compile(r"^ADJECTIVE").search(i) != None:
            i = re.compile(r"^ADJECTIVE").sub(adj, i)
            sakubun_out.append(i)
        elif re.compile(r"^NOUN").search(i) != None:
            i = re.compile(r"^NOUN").sub(noun, i)
            sakubun_out.append(i)
        elif re.compile(r"^VERB").search(i) != None:
            i = re.compile(r"^VERB").sub(verb, i)
            sakubun_out.append(i)
        elif re.compile(r"^ADVERB").search(i) != None:
            i = re.compile(r"^ADVERB").sub(adv, i) 
            sakubun_out.append(i)
        else:
            sakubun_out.append(i)
    result = " ".join(sakubun_out)
    sakubun_file = open(".\\Automate-the-boring-stuff-with-python\\chapt8\\sakubun_new.txt", "w")
    sakubun_file.write("{}".format(result))
    sakubun_file.close()
    return result

adj = str(input("Enter an adjective:\n"))
noun = str(input("Enter a noun:\n"))
verb = str(input("Enter a verb:\n"))
adv = str(input("Enter an adverb:\n"))

result = sakubun_gen(adj, noun, verb, adv)

print(result)