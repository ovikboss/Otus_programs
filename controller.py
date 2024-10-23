import os
from models import Contacts
from exceptions import ErrorPathName

class Data_file():
    def file_open(self, path:str, cwd:str, container: Contacts) -> None:
        try:
            with open(os.path.join(cwd, path), "r",encoding="utf-8") as data:
                text = data.readlines()
                text = [line.rstrip() for line in text]
                for elem in text:
                    elem = elem.split(", ")
                    container.start(elem[0],elem[1],elem[2])
                print("Файл успешно открыт")
        except Exception as ex:
            raise ErrorPathName("Не удалось открыть файл")

    def save_file(self, path:str, cwd:str, container: Contacts ) -> None:
        try:
            with open(os.path.join(cwd, path), "w",encoding="utf-8") as data:
                for elem in container:
                    data.write(f"{elem.name}, {elem.number}, {elem.coment}\n")
                container.clear_all()
                print("Файл успешно сохранен")
        except Exception as ex:
            print("Не удалось сохранить файл")
            raise ErrorPathName