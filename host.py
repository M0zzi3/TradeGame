import random 

class Host:
    def __init__(self,idd):
        self.idd = idd
        
    def startGame(self):
        self.goldInGame = self.Gold()

    def updateValue(self):
        self.goldInGame.updateValue()
    
    class Gold:
        def __init__(self):
            self.value = 10000
            self.quantity = 2
            self.valueUpdate = 0
            self.stablilityPercent = 0.01

        def buyUpdate(self):
            self.valueUpdate -= self.value * self.stablilityPercent

        def sellUpdate(self):
            self.valueUpdate += self.value * self.stablilityPercent

        def updateValue(self):
            self.value += random.randint(-10, 10)
            self.value += round(self.valueUpdate)
            self.valueUpdate = 0