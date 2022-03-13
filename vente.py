
class Group:

    def __init__(self, key):
        self.key = key
        self.products = {}
        # self.cumul_price = 0

    def getKey(self):
        return self.key

    def getProducts(self):
        return self.products

    def getProduct(self, key):
        if key not in self.products:
            return Product(key)
        return self.products[key]

    def cumul(self, key, price):
        if key not in self.products:
            self.products[key] = Product(key)
        self.products[key].cumul(price)


class Product:

    def __init__(self, key):
        self.key = key
        self.cumul_price = 0

    def cumul(self, price):
        self.cumul_price += price

    def getCumulPrice(self):
        return self.cumul_price
