import random 

class Host:
    def __init__(self,idd):
        self.idd = idd
        
    def startGame(self):
        self.gold = self.Gold()

    def updateValue(self):
        self.gold.updateValue()
    
    class Gold:
        def __init__(self):
            self.value = 100
            self.quantity = 2

        def updateValue(self):
            self.value += random.randint(-10, 10)
