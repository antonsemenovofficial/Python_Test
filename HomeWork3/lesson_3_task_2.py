from smartphone import Smartphone


catalog = ''

gadget1 = Smartphone("Apple", "Iphone 12", "+79999999999")
gadget2 = Smartphone("Xiaomi", "Mi 12", "+79999999988")
gadget3 = Smartphone("Samsung", "A52", "+79999999977")
gadget4 = Smartphone("Nokia", "3310", "+79999999966")
gadget5 = Smartphone("Huawei", "P50", "+79999999955")


catalog = [gadget1, gadget2, gadget3, gadget4, gadget5]

def saycatalog():
    if catalog == []:
        print("Каталог пуст")
    else:
        print(catalog)
