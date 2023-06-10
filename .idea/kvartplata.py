const = int(36.83)
const2 = int(74.38)

waterprice = 41.57
dayprice = 4.21
nightprice = 2.28
wateroutprice = 74.78
energyhotwaterprice = 1600.3
energyforone = 0.066
Coldwater = int(input(' Показания холодной воды '))
Hotwater = int(input(' Показания горячей воды '))
Day = int(input(' Счётчик день '))
Night = int(input (' Счётчик ночь '))
x = ((37.6 * const) + const2) + 220 + 50
e = ((Hotwater * energyforone) * energyhotwaterprice)
h = Hotwater * waterprice
c = Coldwater * waterprice
out = (Coldwater + Hotwater) * wateroutprice
light = (Day * dayprice) + (Night * nightprice)
water = e + h + out + c

kvartplata = x + light + water + 236

print (' Квартплата ' , kvartplata)