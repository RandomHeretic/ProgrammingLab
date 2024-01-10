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
        self.z=self.a
        return self
    def __next__(self):
        while(self.z % self.x !=0):
            self.z+=1
        if self.z > self.b:
            raise StopIteration
        self.z+=1
        return self.z-1


a=list(division(13,88,400))
print(a)
