class Smartphone:
    brend = ""
    model = ""
    number = ""

    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number
    def say(self):
        print("Бренд устройства:", self.brend, "Модель устройства:", self.model, "Номер телефона:", self.number)

gadget1 = Smartphone("Apple", "Iphone 12", "+79999999999")
gadget2 = Smartphone("Xiaomi", "Mi 12", "+79999999988")
gadget3 = Smartphone("Samsung", "A52", "+79999999977")
gadget4 = Smartphone("Nokia", "3310", "+79999999966")
gadget5 = Smartphone("Huawei", "P50", "+79999999955")

