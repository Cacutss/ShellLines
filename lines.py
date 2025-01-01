import random
import os

class LineCreator():
    def __init__(self,amount):
        self.amount = int(amount)
    
    def Createlines(self):
        result = []
        for i in range(self.amount):
            result.append(Line())
        return result

class Line():
    def __init__(self):
        self.limit = os.get_terminal_size()
        self.pos = random.randint(0,self.limit[0])
        self.color = random.randint(31,38)
        self.currentstr = "|"

    def update(self):
        random.seed()
        direction = random.randint(0,20)
        if direction < 19:
            if self.currentstr == "\\":
                self.pos += 1
            elif self.currentstr == "/":
                self.pos -= 1
            self.currentstr = "|"
        else:
            if self.currentstr == "\\":
                self.pos += 1
            elif self.currentstr == "/":
                self.pos -= 1
            if direction == 19 or self.pos + 4 > self.limit[0]:
                self.pos -= 1
                self.currentstr = "/"
            else:
                self.pos += 1
                self.currentstr = '\\'
        if self.pos > self.limit[0]:
            self.pos = self.limit[0]
        elif self.pos < 0:
            self.pos = 0

    def __repr__(self):
        return f'\033[{self.color}m{self.currentstr}\033[0m'
