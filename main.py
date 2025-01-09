from lines import *
import random
import time
import sys
import os

def main():
    random.seed()
    n = random.randint(1,50)
    speed = 0.01
    creator = LineCreator(n)
    lines = creator.Createlines()
    currenty = 0
    os.system('clear')
    while True:
        size = os.get_terminal_size()
        time.sleep(speed)
        string = ""
        sys.stdout.write("\x1B[H")
        for i in range(len(lines)):
            lines[i].update()
            sys.stdout.write(f"\x1B[{currenty};{lines[i].pos}H{lines[i]}")
            sys.stdout.flush()
        if currenty == size[1]:
            sys.stdout.write(f"\n")
        else:
            currenty += 1

if __name__ == "__main__":
    main()
