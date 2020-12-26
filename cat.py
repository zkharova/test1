from . import domestic
class Cat(domestic.Domestic):

    def __init__(self, name):

        super().__init__(name)

    def saySound(self):
        print('звук: ' )