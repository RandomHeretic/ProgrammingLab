class bob:
    def __init__(self,a,b):
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

    def isprime(self,x):
        for i in range(2,x):
            if x%i==0:
                return 0
        return 1
    def __next__(self):
        while(not self.isprime(self.z)):
            self.z+=1
        self.z+=1
        if self.z <= self.b:
            return self.z-1
        raise StopIteration


a=list(bob(2,8))
print(a)

a=list(bob(88,400))
print(a)
