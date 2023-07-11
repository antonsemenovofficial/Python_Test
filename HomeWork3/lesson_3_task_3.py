from mailing import Mailing
from address import Address

to_address4 = (199244, 'Санкт-Петербург', "Бела-Куны", 15, 211)
from_address4 = (188668, "Мурино", "Петровская", 22, 124)

mailing3 = Mailing(to_address4,from_address4, 1500, 'd5456')

mailing3.sayMailing()

