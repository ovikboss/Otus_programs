import os
from models import  Contacts
from controller import Data_file

clear = lambda:os.system("cls")
cwd = os.getcwd()
container = Contacts()
data_manager = Data_file()

def file_open(path:str) -> None:
    try:
        with open(os.path.join(cwd, path), "r",encoding="utf-8") as data:
            text = data.readlines()
            text = [line.rstrip() for line in text]
            for elem in text:
                elem = elem.split(", ")
                container.start(elem[0],elem[1],elem[2])
            print("Файл успешно открыт")
    except Exception as ex:
        print(ex)

def save_file(path:str) -> None:
    try:
        with open(os.path.join(cwd, path), "w",encoding="utf-8") as data:
            for elem in container:
                data.write(f"{elem.name}, {elem.number}, {elem.coment}\n")
            container.clear_all()
            print("Файл успешно сохранен")
    except Exception as ex:
        print("Не удалось сохранить файл")

def main() -> None:
    var = ""
    while var != 8:
        clear()
        print("""1. Открыть файл
2. Сохранить файл
3. Добавить контакт
4. Удалить контакт
5. Показать все контакты
6. Показать контакт
7. Изменить контакт
8. Остановить программу
""".strip())
        try:
            var = int(input())
            match var:
                case 1:
                    path = input("Введите имя файла ")
                    data_manager.file_open(path, cwd, container)
                    input("что бы продолжить введите любой символ")
                case 2:
                    data_manager.save_file(path, cwd, container)
                    input("что бы продолжить введите любой символ")
                case 3:
                    container.add_contact()
                    input("что бы продолжить введите любой символ")
                case 4:
                    id = int(input("Введите id пользователя "))
                    container.remove_con(id)
                    input("что бы продолжить введите любой символ")
                case 5:
                    container.show_all()
                    input("что бы продолжить введите любой символ")
                case 6:
                    name = input("Введите имя ")
                    container.show_con(name)
                    input("что бы продолжить введите любой символ")
                case 7:
                    id = int(input("Введите id пользователя "))
                    param = input("Что будем менять Номер, Имя, Комментарий? ")
                    container.change(id, param)
                    input("что бы продолжить введите любой символ")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    main()
