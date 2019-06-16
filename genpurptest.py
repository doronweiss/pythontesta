r = range (10)  # type: range
#r=[1,2,3,4,5,6,7,8,9]
it = iter(r)
item=next(it, None)
while item is not None:
    print (item)
    item = next(it, None)

factors = lambda  n: [x for x in range (1,n+1) if n % x ==0]

print ("{0}".format(factors(15)))