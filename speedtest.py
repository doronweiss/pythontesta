import time


tstart = time.time()
sum=0
count=1000000
for i in range (count):
    a=i
    b=3
    c = a + b
    sum += c
tend=time.time()
print ("Sum: %d, Time: %f, OpTime: %lf "%(sum, tend-tstart, (tend-tstart)*1000.0/float(count)))