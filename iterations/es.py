class s(int):
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        self.a+=1
        if self.a == 20:
            raise StopIteration
        return self.a
    
import random

class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration
        return 1



b=[eggs for eggs in RandomIterable()]
print(b)
b=list(RandomIterable())
print(b)
a=[i for i in s()]
print(a)
a=list(s())
print(a)
class ss(int):
    def culo(self):
        print('culo')
    def __init__(self):
        print('no')

b=ss()
c=8
print(isinstance(c,ss))
print(c.bit_length())




p='banana'
print(list(p))