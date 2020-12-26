def Fish(Wild):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    def saySound(self):
        print('звук: '+ self.sound)