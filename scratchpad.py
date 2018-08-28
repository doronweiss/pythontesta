"""
str="1,2,3,4,5,6,7,8,9"
vars=str.split(",")
for idx in range(3):
    for jdx in range (3):
        print ("Array[%d,%d]=%d"%(idx+1, jdx+1, int(vars[idx*3+jdx])))

a=1
if 'a' in globals():
    print (a)
else:
    print ("A was deleted")
del a
if 'a' in globals():
    print (a)
else:
    print ("A was deleted")
if 'vars' in globals():
    print (vars)
else:
    print ("vars was deleted")
del vars
if 'vars' in globals():
    print (vars)
else:
    print ("vars was deleted")
"""
ln="doron,jenny,yaniv,,liat,,rorshach"
a = [x for x in ln.split(',') if not len(x.strip())==0]
print (a)
a=[0]*5
print (a)
a[0]=3
print (a)
s="abcdefghijklmnop"
print (s[2:4])
print(s[1::2])
