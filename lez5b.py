
class CSVFile():
    def __init__(self,name):
        self.name=name
        try:
            self.file=open(self.name,"r")
        except:
            print('Errore')    
    def __del__(self):
        try:
            self.file.close()
        except:
            pass
    def get_data(self):
        try:
            self.file.readline()
            a = self.file.readlines()
            b = []
            for item in a:
                c=item.replace('\n','')
                d = c.split(',')
                b.append(d)
            return b
        except:
            return []


class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        data=super().get_data()
        d=[]
        for item in data:
            p=[]
            for t in item:
                if t==item[0]:
                    p.append(t)
                else:
                    try:
                        p.append(float(t))
                    except:
                        print('Errore')
            d.append(p)
            
        return d
c=CSVFile('shampoo_sales.csv')
print(c.get_data())
cc=NumericalCSVFile('shampoo_sales.csv')
print(cc.get_data())