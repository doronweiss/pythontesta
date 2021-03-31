import json


class JClass:
    def __init__(self):
        self.fname = "doron"
        self.lname = "weiss"
        self.age = 59
        self.data=[1,2,3,4,5]


a = ['1', '2', '3', '4', '5']
print(a)
b = json.dumps(a)
print(b)
jc = JClass()
b = json.dumps(jc.__dict__)
print(b)
str = '{"fname": "doron", "lname": "weiss", "age": 59, "data": [1, 2, 3, 4, 5]}'
jc2 = json.loads(str)
print (jc2)