class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self,name):
         # metodo init
        self.name=name
        
        if not isinstance(self.name,str): # controllo che mi sia stata data una stringa
            raise ExamException('file name not str')    

    
    def check_date(self,date):
         # metodo per controllare se una stringa è una data Anno-Mese
        date = date.split('-')
        
        try:
            date[0]=float(date[0])
            date[1]=float(date[1])
            
            if len(date) == 2 and date[0]%1==0 and date[1]%1==0 and date[0]>0 and date[1]>0 and date[1]<13:
                return 1
        except:
            pass
        return 0

    
    def check_value(self,value):
         # metodo per controllare se un valore è intero non nullo e positivo
        try:
            value=float(value)
        except:
            return 0
        if value%1 != 0 or value <= 0:
            return 0
        return 1

    
    def check_duplicate(self,data):
         # metodo per controllare se in una lista di time_series ho duplicati
        for i in range(0,len(data)):
            for j in range (i+1,len(data)):
                if data[i][0]==data[j][0]:
                    return 1
        return 0

    
    def check_order(self,data):
         # metodo per controllare se una lista di time_series è in ordine temporale
        dates=[]
        for i in data:
            dates.append(i[0].split('-'))
        for i in range(0,len(dates)):
            for j in range(i+1,len(dates)):
                
                if dates[i][0]>dates[j][0]:
                    return 1
                
                if dates[i][0]==dates[j][0] and dates[i][1]>=dates[j][1]:
                    return 1
        return 0

    
    def get_data(self):# metodo get_data
        try:
            file=open(self.name,'r') # provo ad aprire il file dato nel metodo init
        except:
            raise ExamException('file not found')

        all=file.readlines() # prendo tutte le righe del file
        output=[] # variabile dove inserirò l'output
        
        for item in all: # guardo ogni riga cercando le informazioni che mi interessano
            
            buffer=item.replace('\n','').split(',')
            
            if len(buffer) >= 2:
                if self.check_date(buffer[0])==1 and self.check_value(buffer[1]):
                    output.append(buffer)
        
        if self.check_duplicate(output): # controllo duplicati
            raise ExamException('multiple data for one month')
        
        if self.check_order(output): # controllo ordine
            raise ExamException('data not in order')
        
        return output




def compute_increments(time_series,first_year,last_year): # funzione per gli incrementi
    if not isinstance(first_year,str) or not isinstance(last_year,str):
        raise ExamException('invalid extremes, they should be strings')
    
    for i in time_series: # controllo che i dati che mi sono stati dati siano validi
        try:
            i[1]=float(i[1])
            if i[1]%1 != 0 or i[1] <= 0:
                raise ExamException('time_series_error, incorrect value foud')
        except:
            raise ExamException('time_series_error, incorrect value foud')
        try:
            time_stamp=i[0].split('-')
            time_stamp[0]=float(time_stamp[0])
            time_stamp[1]=float(time_stamp[1])
            if len(time_stamp) != 2 or time_stamp[0]%1!=0 or time_stamp[1]%1!=0 or time_stamp[0]<1 or time_stamp[1]<1 or time_stamp[1]>12:
                raise ExamException('time_series_error, incorrect time stamp foud')
        except:
            raise ExamException('time_series_error, incorrect time stamp foud')
    
    f=0 # variabile a fini di controllo
    l=0 # variabile a fini di controllo
    d={} # dizionario temporneo
    
    for i in time_series: # cerco per gli anni richiesti
        if i[0].split('-')[0] == first_year:
            f=1
        if f==1 and l==0:
            if d.get(i[0].split('-')[0]) is None: 
                 # se un anno non è nel dizionario lo aggiungo
                d.update({i[0].split('-')[0]: [int(i[1]),1]})
            else:
                 # se c'è già lo aggiorno aggiungendo un mese e il numero di passeggeri
                sup=d.get(i[0].split('-')[0])
                sup[0] += int(i[1])
                sup[1] += 1
                d.update({i[0].split('-')[0]: sup})
        if i[0].split('-')[0] == last_year:
            l=1
    
    if l==0 or f==0 or first_year==last_year:
         # se non trovo l'inizio o la fine dell'intervallo 
         # o se questo è tra lo stesso anno alzo un errore
        raise ExamException('invalid extremes, not found in time_series')
    
    ind=[] # array dove inserisco gli indirizzi del dizionario
    for i in d:
        ind.append(i)
        d[i]=d[i][0]/d[i][1] # media valori
    
    out={} # variabile per l'output
    for i in range(0,len(ind)-1): # calcolo l'output
        stringa=ind[i]+'-'+ind[i+1]
        value=d.get(ind[i+1])-d.get(ind[i])
        out.update({stringa:value})
    return out