
class CSVFile():
    def __init__(self,name):
        self.name=name
        if not isinstance(self.name,str):
            raise Exception("file non esistente")    
    def get_data(self,start=None,end=None):

        #controlli vari e sanitiazzazione
        
        try:
            self.file=open(self.name,"r")
        except:
            print('Errore')

        
        try:
            a = self.file.readlines()
        except:
            return []

        
        if start is not None:
            if not isinstance(start,int):
                try:
                    start=int(float(start))
                except:
                    pass
                if not isinstance(start,int):
                    raise Exception('start not integer')
            if start < 1:
                raise Exception('start less than 1')
            if start > len(a):
                raise Exception("start larger than file")
        else:
            start=1
            
        if end is not None:
            if not isinstance(end,int):
                try:
                    end=int(float(end))
                except:
                    pass
                if not isinstance(end,int):
                    raise Exception('end not integer')
            if end < start:
                raise Exception('end less than start')
            if end>len(a):
                raise Exception('end larger than file')
        else:
            end=len(a)
        
        #esecuzione
        
        b = []
        for item in range(start-1,end):
            c = a[item].replace('\n','')
            d = c.split(',')
            if d[0] != 'Date':
                b.append(d)
        self.file.close()
        return b