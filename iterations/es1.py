class mid:
    def __init__(self,x,y):
        try:
            self.x=float(x)
        except:
            raise
        if self.x < 0:
            raise Exception('x less than 0')
        try:
            self.y=float(y)
        except:
            raise
        if self.y < self.x:
            raise Exception('y less than x')
        self.z=x
    def __iter__(self):
        return self
    def __next__(self):
        if self.z<=self.y and self.z+self.x<self.y:
            self.z+=1
            return self.z-1
        raise StopIteration



a=list(mid(8,20))
print(a)
a=list(mid(8,8))
print(a)
try:
    a=list(mid(20,2))
    print(a)
except Exception as e:
    print(e)
try:
    a=list(mid(8,'20'))
    print(a)
except Exception as e:
    print(e)
try:
    a=list(mid(8,'s'))
    print(a)
except Exception as e:
    print(e)
try:
    a=list(mid(-8,8))
    print(a)
except Exception as e:
    print(e)
a=list(mid(0,2))
print(a)