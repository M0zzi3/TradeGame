import random

class Host:
    def __init__(self):
        self.id = random.randint(100000,999999) #rboić zabezpieczenie aby się nie powtarzały
    