import os
from pprint import pprint

def main():
    dirs = []
    target_dir = "../sub"

    for i in os.listdir(target_dir):
        dirs.append(os.path.join(target_dir, i))


    for p in dirs:
        with open(p, "r") as f:
            ret = f.readlines()
    return ret

