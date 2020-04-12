import time, sys
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

print("Version: %s" % (np.__version__))
a1 = np.array([1, 2, 3])
a2 = np.array([2, 3, 4])
print("Element wise => {}".format(a1 * a2))
print("LinAlg wise => {}".format(a1 @ a2))
av = np.vstack((a1, a2))
print("av => {}".format(av))
ah = np.hstack((a1, a2))
print("ah => {}".format(ah))
sys.exit(0)


a = 30

d2r = np.pi / 180.0
ar = a * d2r

tmat = np.array([[np.cos(ar), np.sin(ar), 1], [-np.sin(ar), np.cos(ar), 1], [np.sin(ar), -np.cos(ar), 1]])
# a = np.matrix([[1,2,3],[3,4,5],[1,0,13]])
print(tmat)
print("Mat mult :")
print(tmat * tmat.transpose())
print("Determinant :", end="")
print(np.linalg.det(tmat))

# speed test
cnt = 100
start = time.time()
for i in range(1, cnt):
    c = tmat * tmat;
print("Matrix mult {} times, Elapsed: {} => {}".format(cnt, time.time() - start, c))

start = time.time()

vec = np.array([1.0, 0.0, 0.0])
vec2 = np.array([0.0, 1.0, 0.0])
print(tmat @ vec)
print(np.cross(vec, vec2))

print("Elapsed: %s" % (time.time() - start))

# plottinh
r = range(101)
x = [0] * 101
y = [0] * 101
for i in r:
    x.append(i / 10.0)
    y.append(np.sin(i / 10.0))
plt.plot(x, y)
plt.ylabel('Sinus')
# plt.show()

f = lambda x: x * x


def myf(x):
    return np.sin(x)


print("Lambda 30 = {0}".format(f(30)))

i = spint.quad(myf, 0, np.pi)
print("Integration: i= {}".format(i))
i = spint.quad(lambda z: np.sin(z), 0, np.pi)
print("lambga Integration: i= {}".format(i))
