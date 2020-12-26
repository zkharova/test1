from . import domestic

class Dog(domestic.Domestic):

    def __init__(self, name):

        super().__init__(name)
