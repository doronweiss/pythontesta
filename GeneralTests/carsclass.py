class Car(object):
    #weight: int=1200

    def __init__(self, weight):
        self.weight=weight

    def speed (self):
        if self.weight<1500:
            return 130
        else:
            return 90