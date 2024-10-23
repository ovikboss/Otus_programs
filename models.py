class User:
    id = 0
    def __init__(self, name, number, coment) -> None:
        self.name = name
        self.number = number
        self.coment = coment
        self.id = User.id
        User.id += 1
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nИмя: {self.name}\nНомер: {self.number}\nКоментарий: {self.coment}"

class Contacts:
    lst = []
    def new_contact(self):
        name = input("Введите имя ")
        number = int(input("Введите номер телефона "))
        coment = input("Введите коментарий ")
        self.lst.append(User(name, number, coment))
    
    def start(self, name, number, coment):
        self.lst.append(User(name, number, coment))
    
    def __iter__(self):
        return iter(self.lst)