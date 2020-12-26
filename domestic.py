from . import animal


class Domestic(animal.Animal):
    def __init__(self, name):
        self.name = name
