class Model:
    def __init__(self,window):
        self.window=window
    def fit(self):
        raise NotImplementedError
    def predict(self):
        raise NotImplementedError
    def evaluate(self,data):
        try:
            sanitize(data)
        except:
            raise
        wiwo=len(data)-self.window
        if wiwo <= 0:
            raise Exception
        for_fit=data[:wiwo]
        for_test=data[wiwo:]
        try:
            self.fit(for_fit)
        except Exception as e:
            if isinstance(e,NotImplementedError):
                pass
            else:
                raise
        eval_mae=0
        for i in range(0,len(for_test)-3):
            pred=self.predict(for_test[i:i+3])
            eval_mae+= abs(pred-for_test[i+4])
        return eval_mae
def sanitize(data):
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
    return data
def p(data):
    try:
        sanitize(data)
    except:
        raise
    prev_data = None
    dev=0
    for item in data:
        if prev_data is not None:
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















