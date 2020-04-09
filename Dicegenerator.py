import random
class Dice:
    def __init__(self):
        self.number=(0,0)
    def roll(self):
        self.number=(random.randint(1,6),random.randint(1,6))
        self.checksum()
    def checksum(self):
        self.sum=self.number[0]+self.number[1]
        if self.sum<7:
            self.c=2
        elif self.sum>7:
            self.c=1
        else:
            self.c=3
    def cal(self,g):
        self.roll()
        if(g==self.c):
            return 1
        else:
            print("Wrong Guess\n")
            return 0
