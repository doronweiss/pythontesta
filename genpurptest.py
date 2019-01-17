r = range (10)  # type: range
#r=[1,2,3,4,5,6,7,8,9]
it = iter(r)
item=next(it, None)
while item is not None:
    print (item)
    item = next(it, None)