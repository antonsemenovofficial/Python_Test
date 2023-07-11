class User:
    def __init__(self, first_name, last_name):
        print("Создано")
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + " " + last_name

    
    def sayName(self):
        print("Мое имя", self.first_name)
    def sayLastName(self):
        print("Моя фамилия" , self.last_name)
    def sayFull(self):
        print("Меня зовут", self.fullname)

user1 = User("Антон", "Семенов")

user1.sayName()
user1.sayLastName()
user1.sayFull()
