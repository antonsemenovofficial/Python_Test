class Smartphone:
    def __init__(self, brend, model, number):
        self.brend = brend
        self.model = model
        self.number = number
    def say(self):
        print("Бренд устройства:", self.brend, "Модель устройства:", self.model, "Номер телефона:", self.number)
    def __str__(self):
        return f'{self.brend}, {self.model}, {self.number}'