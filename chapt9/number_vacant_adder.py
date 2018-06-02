import os, re, shutil

def vcn_adder(path):
    folder = os.path.join(path)
    files = os.listdir(folder)
    i = 0
    for f in files:
        num = "text\d*" + str(i)
        num_t = re.compile(num)
        f_name = str(f)
        if num_t != f_name:
            target_path = folder + num
            shutil.move(f, target_path)
        i += 1
    return True

path = input("Input path:")
result = vcn_adder(path)