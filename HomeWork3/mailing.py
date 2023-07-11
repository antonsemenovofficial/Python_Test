to_address = ''
from_address = ''
cost = ''
track = ''

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
    def sayMailing(self):
        print("Куда:", self.to_address, "Откуда:", self.from_address, "Цена:", self.cost, "Трек-номер:", self.track )

to_address3 = (100112, 'Moscow', 'Street1', 15, 111)
from_address3 = (100112, 'Moscow', 'Street2', 25, 211)
mailing2 = Mailing(to_address3, from_address3, 5, 112233445566)

mailing2.sayMailing()