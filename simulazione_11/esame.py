class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self,window):
        if not isinstance(window,int):
            raise ExamException('window not integer')
        if window < 1:
            raise ExamException('window less than 1')
        self.window=window
    def compute(self,data):
        data=self.sanitize(data)
        c=0
        res=[]
        for i in range(0,len(data)-self.window+1):
            for j in range(0,self.window):
                c+=data[i+j]
            res.append(c/self.window)
            c=0
        return res

    def sanitize(self,data):
        if not isinstance(data,list):
            raise ExamException('input not list')
        if len(data) < self.window:
            raise ExamException('input list shorter than window')
        for i in range(0,len(data)):
            try:
                data[i]=float(data[i])
            except:
                raise ExamException('unsanitizable item found in list')
        return data


try:
    MovingAverage(0.8)
except Exception as e:
    print(e)
try:
    MovingAverage('banana')
except Exception as e:
    print(e)
print('')
mov1=MovingAverage(1)
mov2=MovingAverage(2)
mov3=MovingAverage(3)
mov4=MovingAverage(4)
mov=[mov1,mov2,mov3,mov4]
a=[1,8,5,6,7,8]
#4.5,6.5,5.5,6.5,6.0,6.5
b=['2',25,55,8]
bb=[8,5,'s',8]
c=[]
d=3
dd='cavolo'
e=[1,2]
f=[{1:2},{8:5}]
g=[[2,3,4],[5,6],[444,555],[43]]
gg=[[2,3,4],[5,6],[444,555],[43],3]
h=[1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111]
test=[a,b,bb,c,d,dd,e,f,g,gg,h]
for item in test:
    for m in mov:
        try:
            print(m.compute(item))
        except ExamException as e:
            print(e)
    print('')