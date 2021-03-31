class testclass (object):
    def __init__(self, anum):
        self.number = anum


    def show(self):
        print ("Number = {}".format(self.number))

    def showagain(self):
        print ("Number = {}".format(self.number))


def mydec(func):
    def wrapper_do_twice(s):
        func(s)
        func(s)
    return wrapper_do_twice

@mydec
def prrr(s):
    print (s)

tc = testclass(3)
tc.show()
tc.showagain()
prrr("doron weiss")