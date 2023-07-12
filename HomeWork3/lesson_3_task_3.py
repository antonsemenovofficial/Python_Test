from mailing import Mailing
from address import Address

to_address = Address(199244, 'Санкт-Петербург', "Бела-Куны", 15, 211)
from_address = Address(188668, "Мурино", "Петровская", 22, 124)


mailing = Mailing(to_address,from_address, 1500, 'd5456')

mailing.say_mailing()

