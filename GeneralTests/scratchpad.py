import numpy as np

# l = [[1,2,3],[4,5,6], [7], [8,9]]
# print ("{0}".format(np.array(l).flat))

# str = "the fat dog   jumped over   the fenc  e"
# parts = [x for x in str.split(' ') if x ]
# str2 = " ".join(parts)
# print("{}".format(str))
# print("{}".format(str2))

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)