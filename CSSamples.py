a=list(range(1,100))
print (list(a))
b=filter(lambda n: n%7==0,a)
print (list(b))
c=[x for x in a if x%7==0]
print (c)
d=[x*x for x in a if x%7==0]
print (d)
