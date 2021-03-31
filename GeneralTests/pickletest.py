import pickle


class JClass:
    def __init__(self):
        self.fname = "doron"
        self.lname = "weiss"
        self.age = 59
        self.data = [1, 2, 3, 4, 5]


jc = JClass()
str = pickle.dumps(jc)
print("Dump result: {0}".format(str))
jc2 = pickle.loads(str)
print("Load result: {0}".format(jc2))
