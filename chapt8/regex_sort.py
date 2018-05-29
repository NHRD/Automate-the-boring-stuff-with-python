import re, os

def regex_sercher(rege):
    result_list = []
    file_list = os.listdir(".\\Automate-the-boring-stuff-with-python\\chapt8\\regex_sort_files")
    #print(file_list)
    
    for i in file_list:
        path = ".\\Automate-the-boring-stuff-with-python\\chapt8\\regex_sort_files\\" + i
        text_file = open(path, "r")
        text = text_file.read()
        text_list = text.split("\n")
        regex = "^.*" + rege + ".*$"
        for j in text_list:
            if re.compile((regex)).search(j) != None:
                result_list.append(re.compile((regex)).search(j).group())
        text = text_file.close()

    result = "\n".join(result_list)
    return result

test = regex_sercher(r"Bravo alpha bra")
print(test)