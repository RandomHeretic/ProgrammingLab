from lez9 import FitTrendModel
from matplotlib import pyplot



a=FitTrendModel()
l=[1,2,5,8,9,6,5,3,5,4,8,5,2]
ll=[-1,-2,8,6,3,2,1]+l
a.fit(ll)
p=a.predict(l)

pyplot.plot(ll+[p],color='tab:red')
pyplot.plot(ll,color='tab:blue')
pyplot.show()