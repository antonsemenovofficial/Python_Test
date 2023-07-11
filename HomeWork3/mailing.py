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
<<<<<<< HEAD
    def sayMailing(self):
        print("Куда:", self.to_address, "Откуда:", self.from_address, "Цена:", self.cost, "Трек-номер:", self.track )
=======
 
    def sayMailing(self):
        print(self.to_address, self.from_address, self.cost, self.track)
>>>>>>> f650b7cb37b1914c87ade45da6ee63bf78a4f35d

to_address3 = (100112, 'Moscow', 'Street1', 15, 111)
from_address3 = (100112, 'Moscow', 'Street2', 25, 211)
mailing2 = Mailing(to_address3, from_address3, 5, 112233445566)

<<<<<<< HEAD
=======
mailing2 = Mailing(1, 2, 5, 112233445566)

>>>>>>> f650b7cb37b1914c87ade45da6ee63bf78a4f35d
mailing2.sayMailing()