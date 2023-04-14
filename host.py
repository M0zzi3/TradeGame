import random 

class Host:
    def __init__(self,idd):
        self.idd = idd
        
    def startGame(self):
        self.goldInGame = self.Gold()
        self.days = 4

    def updatePeriod(self):
        self.goldInGame.updateValue()
        self.days -= 1
    
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