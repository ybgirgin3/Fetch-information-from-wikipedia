import os
from pprint import pprint

def main():
    dir = '../sub'
    for i in os.listdir(dir):
        fn = f"{os.path.splitext(i)[0]}_info.txt"

        # dosyayı oku
        with open(os.path.join(dir, i), "r") as f:
            ret = f.readlines()


    #print(fn, ret)
    return fn, ret


#main()



#def main():
#    dirs = []
#    target_dir = "../sub"
#
#    for i in os.listdir(target_dir):
#        dirs.append(os.path.join(target_dir, i))
#
#
#    for p in dirs:
#        with open(p, "r") as f:
#            ret = f.readlines()
#    return ret

