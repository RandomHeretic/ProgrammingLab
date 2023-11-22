class CSVFile():
    def __init__(self,name):
        self.name=name
        self.file=open(self.name,"r")
    def get_data(self):
        self.file.readline()
        a = self.file.readlines()
        b = []
        for item in a:
            #c=item.replace('\n','')
            d = item.split(',')
            b.append(d)
        return b
#csv=CSVFile('shampoo_sales.csv')
#print(csv.get_data())