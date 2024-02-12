class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
        if not isinstance(self.name,str):
            raise ExamException('file name not str')    
    def check_date(self,date):
        d = date.split('-')
        try:
            d[0]=float(d[0])
            d[1]=float(d[1])
            if len(d) == 2 and d[0]%1==0 and d[1]%1==0 and d[0]>0 and d[1]>0 and d[1]<13:
                return 1
        except:
            pass
        return 0
    def check_value(self,value):
        try:
            value=float(value)
        except:
            return 0
        if value%1 != 0 or value <= 0:
            return 0
        return 1
    def check_duplicate(self,data):
        for i in range(0,len(data)):
            for j in range (i+1,len(data)):
                if data[i][0]==data[j][0]:
                    return 1
        return 0
    def check_order(self,data):
        a=[]
        for i in data:
            a.append(i[0].split('-'))
        for i in range(0,len(a)):
            for j in range(i+1,len(a)):
                if a[i][0]>a[j][0]:
                    return 1
                if a[i][0]==a[j][0] and a[i][1]>=a[j][1]:
                    return 1
        return 0
    def get_data(self):
        try:
            file=open(self.name,'r')
        except:
            raise ExamException('file not found')
        a=file.readlines()
        b=[]
        for item in a:
            c=item.replace('\n','').split(',')
            if len(c) >= 2:
                if self.check_date(c[0])==1 and self.check_value(c[1]):
                    b.append(c)
        if self.check_duplicate(b):
            raise ExamException('multiple data for one month')
        if self.check_order(b):
            raise ExamException('data not in order')
        return b

def compute_increments(time_series,first_year,last_year):
    if not isinstance(first_year,str) or not isinstance(last_year,str):
        raise ExamException('invalid extremes, they should be strings')
    for i in time_series:
        try:
            i[1]=float(i[1])
            if i[1]%1 != 0 or i[1] <= 0:
                raise ExamException('time_series_error, incorrect value foud')
        except:
            raise ExamException('time_series_error, incorrect value foud')
        try:
            ts=i[0].split('-')
            ts[0]=float(ts[0])
            ts[1]=float(ts[1])
            if len(ts) != 2 or ts[0]%1!=0 or ts[1]%1!=0 or ts[0]<1 or ts[1]<1 or ts[1]>12:
                raise ExamException('time_series_error, incorrect time stamp foud')
        except:
            raise ExamException('time_series_error, incorrect time stamp foud')
    f=0
    l=0
    d={}
    for i in time_series:
        if i[0].split('-')[0] == first_year:
            f=1
        if f==1 and l==0:
            if d.get(i[0].split('-')[0]) is None:
                d.update({i[0].split('-')[0]: [0,1]})
            else:
                sup=d.get(i[0].split('-')[0])
                sup[1] += 1
                d.update({i[0].split('-')[0]: sup})
        if i[0].split('-')[0] == last_year:
            l=1
    if l==0 or f==0 or first_year==last_year:
        raise ExamException('invalid extremes, not found in time_series')
    for i in d:
        for item in time_series:
            if item[0].split('-')[0]==i:
                d[i][0]=int(d[i][0])+int(item[1])
    for i in d:
        d[i]=d[i][0]/d[i][1]
    out={}
    ind=[]
    for i in d:
        ind.append(i)
    for i in range(0,len(ind)-1):
        stringa=ind[i]+'-'+ind[i+1]
        value=d.get(ind[i+1])-d.get(ind[i])
        out.update({stringa:value})
    return out