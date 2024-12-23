from exceptions import NotValidInput


class Contact:
    """""Класс отвечает за создание модели контакта"""
    id = 0
    def __init__(self, name, number, coment) -> None:
        self.name = name
        self.number = number
        self.coment = coment
        self.id =  Contact.id
        Contact.id += 1
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nИмя: {self.name}\nНомер: {self.number}\nКоментарий: {self.coment}"
    
    def __eq__(self, value: object) -> any:
        if isinstance(value, Contact):
            return self.number, self.name, self.coment == value.number, value.name, value.coment
        else:
            return "Вы сравниваете не обьекты класса контакт"


class Contacts_Collection:
    """Класс отвечает за хранение контактов и действий связанных с ними"""

    lst: list = []
    def new_contact(self) -> None:
        """Метод создает новый экземляр класса на 
        основе введеных данных
        и добавляет список контактов"""

        try:
            name = input("Введите имя ")
            number = int(input("Введите номер телефона "))
            coment = input("Введите коментарий ")
            self.lst.append(Contact(name, number, coment))
        except Exception as ex:
            print(ex)
    
    def start(self, name, number, coment):
        """Метод создает новый экземляр класса
        и добавляет список контактов"""
        self.lst.append(Contact(name, number, coment))
    
    def __iter__(self):
        """Магический метод который нужен для итерации по экзмепляру класса"""
        return iter(self.lst)
    
    def show_all(self) -> list:
        """Метод для прохождения по коллекции и выводу всех елементов коллекции"""
        try:
            return self.lst
        except Exception as ex:
            print("Ошибка")
    
    def show_con(self, name: str) -> any:
        """Метод для прохождения по коллекции и выводу контакта с поиском по имени"""
        try:
            for elem in self.lst:
                if elem.name == name:
                    return elem
            else:
                return "Контакт не найден"
        except Exception as ex:
            print()

    def remove_con(self) -> str:
        """Метод для прохождения по коллекции и удалению контакта из коллекции с поиском по ID"""
        try:
            id = int(input("Введите id пользователя "))
            for elem in self.lst:
                if elem.id == id:
                    self.lst.remove(elem)
                    return f"Пользователь {elem.name} удален"
            else:
                return "Такого пользователя нет"
        except Exception as ex:
            try:
                raise NotValidInput("Id должно быть числом")
            except NotValidInput as ex:
                return  str(ex)

    def change(self, id:int, param:str)->str:
        """данный метод принимает параметр после чего проходиться по коллекции
        после чего меня параметр который принимала с консоли"""
        try:
            for elem in self.lst:
                if elem.id == id:
                    match param:
                        case "Номер":
                            elem.number = int(input("Введите новый номер "))
                            return f"Пользователь {elem.name} изменен"

                        case "Имя":
                            elem.name = input("Введите новое имя ")
                            return f"Пользователь {elem.name} изменен"

                        case "Комментарий":
                            elem.coment = input("Введите новый комментарий ")
                            return f"Пользователь {elem.name} изменен"

            else:
                return "Такого пользователя нет"
        except Exception as ex:
            try:
                raise NotValidInput("Id должно быть числом")
            except NotValidInput as ex:
                print(ex)

    def clear_all(self) -> None:
        """метод для очистки коллеции"""
        self.lst.clear()
        Contact.id = 0
        
