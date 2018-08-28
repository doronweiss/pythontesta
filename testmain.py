from carsclass import *


class dwc1(object):
    v1 = 3;

    def do(self):
        return self.v1 * 2.5


"""
for i in [1, 2 ,3 ,4 ,5 ,6 ,7]:
    print i
objs = [dwc1() for i in range(10)]
for i in range(10):
    objs[i].v1=2.5+i
for i in range(10):
    print str(objs[i].v1)
"""
cr = Car(weight=870)
#cr.weight=870
print (str(cr.speed()))
cr = Car(weight=2000)
#cr.weight=870
print (str(cr.speed()))
