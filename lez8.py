

class TrendModel:
    
    def predict(self,data):
        #controllo data
        if not isinstance(data,list):
            raise TypeError
        for i in range(0,len(data)):
            try:
                data[i]=float(data[i])
            except KeyError:
                raise
            except ValueError:
                raise
            except Exception:
                raise
        
        prev_data = None
        dev=0
        for item in data:
            if prev_data != None:
                    dev += (item-prev_data)
            prev_data=item
        try:
            return (dev/(len(data)-1))+prev_data
        except ZeroDivisionError:
            raise Exception('un solo elemento')

