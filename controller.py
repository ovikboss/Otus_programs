import os
from models import Contacts_Collection
from exceptions import ErrorPathName

class Data_file():
    """Класс отвечает за открытие, чтение , запись, и закрытие файлов"""
    def file_open(self, path:str, cwd:str, container: Contacts_Collection) -> None:
        """Открывает файл и сохраняет все данные 
        из него ввиде пользователей(контактов)
        после чего закрывает его"""

        try:
            with open(os.path.join(cwd, path), "r",encoding="utf-8") as data:
                text = data.readlines()
                text = [line.rstrip() for line in text]
                for elem in text:
                    elem = elem.split(", ")
                    container.start(elem[0],elem[1],elem[2])
                print("Файл успешно открыт")
        except Exception as ex:
            try:
                raise ErrorPathName("Не удалось открыть файл")
            except ErrorPathName as ex:
                print(ex)

    def save_file(self, path:str, cwd:str, container: Contacts_Collection ) -> None:
        """Открывает файл на запись после чего переводит 
        всех пользоватей из коллекции в формат 
        под запись, после чего закрывает файл"""
        try:
            with open(os.path.join(cwd, path), "w",encoding="utf-8") as data:
                for elem in container:
                    data.write(f"{elem.name}, {elem.number}, {elem.coment}\n")
                container.clear_all()
                print("Файл успешно сохранен")
        except Exception as ex:
            try:
                raise ErrorPathName("Не удалось сохранить файл")
            except ErrorPathName as ex:
                print(ex)
            