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

to_address1 = Address(111000, "Moscow", "Sadovay", 15, 122)
from_address1 = Address(111222, "Moscow", "Sadovay", 22, 333)

to_address1.sayadressto()
from_address1.sayaddressfrom()

