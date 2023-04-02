class User:
    def __init__ (self,useridd):
        self.idd = useridd
        self.walletContents = {"gold":0}

    def setsettings (self,money):
        self.money = money
