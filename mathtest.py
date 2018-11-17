import time
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt


print ("Version: %s"%(np.__version__))

a=30

d2r=np.pi/180.0
ar=a*d2r

tmat=np.matrix ([[np.cos(ar), np.sin(ar),1], [-np.sin(ar), np.cos(ar), 1], [np.sin(ar), -np.cos(ar), 1]])
#a = np.matrix([[1,2,3],[3,4,5],[1,0,13]])
print (tmat)
print ("Mat mult :")
print (tmat*tmat.transpose())
print ("Determinant :", end="")
print (np.linalg.det(tmat))

#speed test
cnt=100
start = time.time()
for i in range(1,cnt):
    c = tmat*tmat;
print ("Matrix mult %d times, Elapsed: %s"%(cnt, time.time() - start))



start = time.time()

vec = np.array ([1.0, 0.0, 0.0])
vec2 = np.array ([0.0, 1.0, 0.0])
print (tmat.dot(vec))
print (np.cross(vec,vec2))

print ("Elapsed: %s"%(time.time() - start))

# plottinh
r = range(101)
x = [0] * 101
y = [0] * 101
for i in r:
    x.append(i / 10.0)
    y.append(np.sin(i / 10.0))
plt.plot(x, y)
plt.ylabel('Sinus')
#plt.show()

f= lambda x:np.sin(x)

def myf (x):
    return np.sin(x)

i = spint.quad(myf, 0, np.pi)
print ("Integration: i= {}".format(i))
