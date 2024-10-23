import os
from models import  Contacts

clear = lambda:os.system("cls")
cwd = os.getcwd()
container = Contacts()

def file_open(path):
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

def save_file(path):
    try:
        with open(os.path.join(cwd, path), "w",encoding="utf-8") as data:
            for elem in container:
                data.write(f"{elem.name}, {elem.number}, {elem.coment}\n")
            container.lst.clear()
            print("Файл успешно сохранен")
    except Exception as ex:
        print("Не удалось сохранить файл")

def add_contact():
    try:
        container.new_contact()
    except Exception as ex:
        print("Не правильный ввод")

def remove_con(id):
    try:
        for elem in container:
            if elem.id == id:
                container.lst.remove(elem)
                print(f"Пользователь {elem.name} удален")
                break
        else:
            print("Такого пользователя нет")
    except Exception as ex:
        print(ex)

def show_all():
    try:
        for elem in container:
            print(elem)
    except Exception as ex:
        print("Ошибка")

def show_con(name):
    try:
        for elem in container:
            if elem.name == name:
                print(elem)
                break
        else:
            print("Контакт не найден")
    except Exception as ex:
        print(ex)

def change(id, param):
    try:
        for elem in container:
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
        print(ex)

def main():
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
                    file_open(path)
                    input("что бы продолжить введите любой символ")
                case 2:
                    save_file(path)
                    input("что бы продолжить введите любой символ")
                case 3:
                    add_contact()
                    input("что бы продолжить введите любой символ")
                case 4:
                    id = int(input("Введите id пользователя "))
                    remove_con(id)
                    input("что бы продолжить введите любой символ")
                case 5:
                    show_all()
                    input("что бы продолжить введите любой символ")
                case 6:
                    name = input("Введите имя ")
                    show_con(name)
                    input("что бы продолжить введите любой символ")
                case 7:
                    id = int(input("Введите id пользователя "))
                    param = input("Что будем менять? ")
                    change(id, param)
                    input("что бы продолжить введите любой символ")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    main()
