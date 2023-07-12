class Address:
    def __init__(self, index, city, street, build, flat):
        self.index = index
        self.city = city
        self.street = street
        self.build = build
        self.flat = flat
    def say_adress_to(self):
        print(self.index, self.city, self.street, self.build, self.flat)
    def say_address_from(self):
        print(self.index, self.city, self.street, self.build, self.flat)
    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.build}, {self.flat}'

