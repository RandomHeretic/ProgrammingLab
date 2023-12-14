class Model:
    def fit(self):
        raise NotImplementedError
    def predict(self):
        raise NotImplementedError

def p(data):
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

class TrendModel(Model):
    def predict(self,data):
        #controllo data
        return p(data)

class FitTrendModel(TrendModel):
    def fit(self,data):
        self.var_glob = p(data) - data[-1]
    def predict(self, data):
        return ((p(data)-data[-1])+self.var_glob)/2+data[-1]
