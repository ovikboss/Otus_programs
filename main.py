import os
from models import  Contacts

clear = lambda:os.system("cls")
cwd = os.getcwd()
container = Contacts()

def fileopen(path):
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

def savefile(path):
    try:
        with open(os.path.join(cwd, path), "w",encoding="utf-8") as data:
            for elem in container:
                data.write(f"{elem.name}, {elem.number}, {elem.coment}\n")
            print("Файл успешно сохранен")
    except Exception as ex:
        print("Не удалось сохранить файл")

def addcontact():
    try:
        container.newcontact()
    except Exception as ex:
        print("Не правильный ввод")

def removecon(id):
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

def showall():
    try:
        for elem in container:
            print(elem)
    except Exception as ex:
        print("Ошибка")

def showcon(name):
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
    while True:
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
        var = int(input())
        match var:
            case 1:
                path = input("Введите имя файла ")
                fileopen(path)
                input("что бы продолжить введите любой символ")
            case 2:
                savefile(path)
                input("что бы продолжить введите любой символ")
            case 3:
                addcontact()
                input("что бы продолжить введите любой символ")
            case 4:
                id = int(input("Введите id пользователя "))
                removecon(id)
                input("что бы продолжить введите любой символ")
            case 5:
                showall()
                input("что бы продолжить введите любой символ")
            case 6:
                name = input("Введите имя ")
                showcon(name)
                input("что бы продолжить введите любой символ")
            case 7:
                id = int(input("Введите id пользователя "))
                param = input("Что будем менять? ")
                change(id, param)
                input("что бы продолжить введите любой символ")
            case 8:
                break

if __name__ == "__main__":
    main()
