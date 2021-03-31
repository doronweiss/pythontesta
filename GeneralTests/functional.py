import numpy as np
import matplotlib.pyplot as plt
import functools as ft

# xs=[x/10.0 for x in range(0,100)]
# ys=[np.sin(x) for x in xs]
#
# plt.plot(xs, ys)
# plt.ylabel('Sinus')
# plt.show()

l = [1, 2, 3, 4, 5]
lm=map((lambda  x:x*x), l)
print ("l mapped sq")
print (*lm, sep=',')
list(range(-5,5))
l2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
l2f= list( filter((lambda x: x <= 0), l2))
print ("l2 filtered")
print (*l2f, sep=',')
lm=map((lambda  x:-x if x<0 else x), l2)
print ("l2 mapped")
print (*lm, sep=',')
lm=ft.reduce((lambda  x,y: x if y==0 else x*y), l2)
print ("l2 reduced")
print (lm, sep=',')
print ("**********************************")
ls = sorted (l2, key=lambda x:x*x)
print ("l2 sorted")
print (*ls, sep=',')
