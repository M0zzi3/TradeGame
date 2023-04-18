class User:
    def __init__ (self,useridd,name):
        self.idd = useridd
        self.walletContents = {"gold":0}
        self.name = name

    def setsettings (self,money):
        self.money = money
