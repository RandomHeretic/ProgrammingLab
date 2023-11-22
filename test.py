class Sabbia():

    def __init__(self, massa, volume):
        self.massa=massa
        self.volume=volume
    
    def __str__(self):
        return 'sabbia {} {}'.format(self.massa,self.volume)

class Sabbietta(Sabbia):
    def __str__(self):
        return 'sabbietta {} {}'.format(self.massa,self.volume)


class Testo(str):
    def __len__(self):
        return len(self.split('a'))
    pass
#################################
s=Sabbia(2,3)
print(s)
ss=Sabbietta(4,6)
print(ss)
t=Testo('Banana asda deosnd pejfjfja kdndjd')
print(len(t))
