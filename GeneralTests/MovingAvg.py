import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import itertools
import functools

krnl=[0.006, 0.061, 0.242, 0.383, 0.242, 0.061, 0.006]

def smooth (lst, i):
    sum = lst[i-3]*krnl[0] +lst[i-2]*krnl[1] + lst[i-1]*krnl[2] + lst[i]*krnl[3] + lst[i+1]*krnl[4] + lst[i+2]*krnl[5] + lst[i+3]*krnl[6]
    return sum

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

rs=[sp.rand() for i in range(100)]
tmps=[rs[0], rs[1], rs[2], [smooth(rs,i) for i in range(3, len(rs)-3)], rs[-3], rs[-2], rs[-1]]
smts=flatten(tmps)
print("{0}".format(rs))
xs=range(100)
plt.plot (xs, rs, 'b')
plt.plot (xs, smts, 'r')
plt.show()
