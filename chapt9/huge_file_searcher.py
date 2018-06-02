import os

def huge_file_searcher(path):
    target = os.path.join(path)
    for root, di, files in os.walk(target):
        for f in files:
            size = os.path.getsize(f)
            print(size)
            if size > 100:
                print(os.path.join(root, f))
    return True

path = input("Input serach target path:")
result = huge_file_searcher(path)