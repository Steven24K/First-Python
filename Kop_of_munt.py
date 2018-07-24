import random

class Node():
    def __init__(self, value, tail):
        self.Value = value
        self.Tail = tail
    def IsEmpty(self):
        return False
    def __str__(self):
        return "(" + str(self.Value) + "," + str(self.Tail) + ")"
    def select(self):
        x = random.randint(0,1)
        for i in range(x):
            self = self.Tail
        return self.Value


class Empty():
    def IsEmpty(self):
        return True
    def __str__(self):
        return ""

empty = Empty()

kop_of_munt = Node("K", Node("M", empty))

for i in range(20):
    a = kop_of_munt.select()
    if a == "K":
        print("Kop")
    else: 
        print("Munt")