index = ''
city = ''
street = ''
build = ''
flat = ''
class Address:
    def __init__(self, index, city, street, build, flat):
        self.index = index
        self.city = city
        self.street = street
        self.build = build
        self.flat = flat
    def sayadressto(self):
        print(self.index, self.city, self.street, self.build, self.flat)
    def sayaddressfrom(self):
        print(self.index, self.city, self.street, self.build, self.flat)

