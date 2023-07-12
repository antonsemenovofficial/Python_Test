from address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.cost = cost
        self.track = track
        self.to_address = to_address
        self.from_address = from_address
    def say_mailing(self):
        print("Куда:", self.to_address, "Откуда:", self.from_address, "Цена:", self.cost, "Трек-номер:", self.track )