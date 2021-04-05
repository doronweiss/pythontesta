''' Exercise #8. Python for Engineers.'''
class JungleThing:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Lion(JungleThing):
    def __init__(self, vel, power):
        super().__init__("Lion", "Predetor")
        # self.name="Lion"
        # self.type="Predetor"
        self.vel=vel
        self.power=power

    def __repr__(self):
        return self.name + "/" + self.type + "/"+ str(self.vel) + "/" + str(self.power)


c = Lion(55,12)
print (c)
