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

