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