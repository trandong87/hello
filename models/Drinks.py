class Drinks:

    def __init__(self, name = None, code = None, image = None, price = None, total = None):
        self.name = name
        self.code = code
        self.image = image
        self.price = price
        self.total = total

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getImage(self):
        return self.image

    def getPrice(self):
        return self.price

    def getTotal(self):
        return self.total