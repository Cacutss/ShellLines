from lines import *
import time
import sys

def main():
    creator = LineCreator(2)
    lines = creator.Createlines()
    currenty = 0
    while True:
        time.sleep(0.05)
        string = ""
        for i in range(len(lines)):
            lines[i].update()
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (currenty,lines[i].pos,f"{lines[i]}"))
            sys.stdout.flush()
        currenty += 1

if __name__ == "__main__":
    main()
