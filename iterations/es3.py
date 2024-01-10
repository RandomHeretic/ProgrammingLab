class division:

    def __init__(self,x,a,b):
        try:
            self.x=int(x)
        except:
            raise
        try:
            self.a=int(a)
        except:
            raise
        try:
            self.b=int(b)
        except:
            raise
        if b<a:
            raise Exception('b<a')
    def __iter__(self):
        self.z=self.a - (self.a % self.x) + self.x
        if self.a%self.x==0:
            self.z-=self.x
        return self
    def __next__(self):
        if self.z <= self.b:
            self.z+=self.x
            return self.z-self.x
        raise StopIteration

a=list(division(2,88,400))
print(a)

a=list(division(13,88,400))
print(a)
