import numpy as np
import matplotlib.pyplot as plt



# r=range(0,101)
# x=[ k for k in r ]
# y=[ np.sin(k) for k in r ]
# plt.plot(x,y, 'r')
# plt.axis([0, 6, 0, 20])
# plt.show()


def makecoeffs (y0, y1, v0, v1):
  a1=a0=0
  dp=y1-y0
  vs = v0+v1
  dy=y1+y0
  da=a1-a0
  b=[y0, v0, 0.0, 10*dy+6*v0-4*v1, -15*dy + 8*v0+7*v1, 6*dy-3*(v1-v0)]
  return b

def calcvalues(b, x):
  x2 = x*x
  x3 = x2 * x
  x4 = x3 * x
  x5 = x4 * x
  y = b[0] + b[1] * x + b[2] * x2 + b[3] * x3 + b[4] * x4 + b[5] * x5
  v = b[1] + 2 * b[2] * x + 3 * b[3] * x2 + 4 * b[4] * x3 + 5 * b[5] * x4
  a = 2 * b[2] + 6 * b[3] * x + 12 * b[4] * x2 + 20 * b[5] * x3
  return y,v,a


coeffs = makecoeffs(1, 3, 10, 15)
print (coeffs)
m=[]
s=[]
vs=[]
accs=[]
for idx in range(0,101):
  m=m+[idx/100]
  y,v,a=calcvalues(coeffs, idx/100)
  s=s+[y]
  vs=vs+[v]
  accs=accs+[a]
plt.plot(m,s, 'r')
plt.show()
plt.plot(m,vs, 'r')
plt.show()
plt.plot(m,accs, 'r')
plt.show()
#print (m)
#print (s)
