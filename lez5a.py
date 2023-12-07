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
            pass

#csv=CSVFile('shampoo_sales.csv')
#print(csv.get_data())