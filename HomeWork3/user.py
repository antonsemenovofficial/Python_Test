class User:
    def __init__(self, first_name, last_name):
        print("Создано")
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    
    def say_name(self):
        print("Мое имя", self.first_name)
    def say_last_name(self):
        print("Моя фамилия" , self.last_name)
    def say_full(self):
        print("Меня зовут", self.full_name)
