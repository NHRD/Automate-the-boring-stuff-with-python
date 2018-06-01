import os, shutil, re

def file_searcher(path_r, path_c):
    target = re.compile(r"\.(pdf|txt)")
    root_path = os.path.join(path_r)
    target_path = os.path.join(path_c)
    print("Copied files are:")
    for root, dir, files in os.walk(root_path):
        for f in files:
            if target.search(f) != None:
                result_f = os.path.join(root, f)
                shutil.copy(result_f, target_path)
                print(f)
    return True

root = input("Input root folder path:")
target = input("Input copy target folder path:")
test = file_searcher(root, target)

while True:
    input("Input any key to quit.:")
    break