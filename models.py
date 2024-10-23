from exceptions import NotValidInput

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
    def new_contact(self) -> None:
        try:
            name = input("Введите имя ")
            number = int(input("Введите номер телефона "))
            coment = input("Введите коментарий ")
            self.lst.append(User(name, number, coment))
        except Exception as ex:
            print(ex)
    
    def start(self, name, number, coment):
        self.lst.append(User(name, number, coment))
    
    def __iter__(self):
        return iter(self.lst)
    
    def show_all(self) -> None:
        try:
            for elem in self.lst:
                print(elem)
        except Exception as ex:
            print("Ошибка")
    
    def show_con(self, name: str) -> None:
        try:
            for elem in self.lst:
                if elem.name == name:
                    print(elem)
                    break
            else:
                print("Контакт не найден")
        except Exception as ex:
            print()

    def remove_con(self) -> None:
        try:
            id = int(input("Введите id пользователя "))
            for elem in self.lst:
                if elem.id == id:
                    self.lst.remove(elem)
                    print(f"Пользователь {elem.name} удален")
                    break
            else:
                print("Такого пользователя нет")
        except Exception as ex:
            try:
                raise NotValidInput("Id должно быть числом")
            except NotValidInput as ex:
                print(ex)

    def change(self, id:int, param:str)->None:
        try:
            for elem in self.lst:
                if elem.id == id:
                    match param:
                        case "Номер":
                            elem.number = int(input("Введите новый номер "))
                            print(f"Пользователь {elem.name} изменен")
                            break
                        case "Имя":
                            elem.name = input("Введите новое имя ")
                            print(f"Пользователь {elem.name} изменен")
                            break
                        case "Комментарий":
                            elem.coment = input("Введите новый комментарий ")
                            print(f"Пользователь {elem.name} изменен")   
                            break                
            else:
                print("Такого пользователя нет")
        except Exception as ex:
            try:
                raise NotValidInput("Id должно быть числом")
            except NotValidInput as ex:
                print(ex)

    def clear_all(self) -> None:
        self.lst.clear()
        User.id = 0
        