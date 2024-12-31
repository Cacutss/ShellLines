import random
import os

class LineCreator():
    def __init__(self,amount):
        self.amount = amount
    
    def Createlines(self):
        result = []
        for i in range(self.amount):
            result.append(Line())
        return result

class Line():
    def __init__(self):
        self.limit = os.get_terminal_size()
        self.pos = random.randint(0,self.limit[0])
        self.space = ""
        self.color = random.randint(31,38)
        self.currentstr = "|"

    def update(self):
        self.space = ""
        self.space += " " * self.pos

    def __repr__(self):
        return f'\033[{self.color}m{self.currentstr}\033[0m'
