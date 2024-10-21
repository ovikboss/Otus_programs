import os
from models import  Contacts

clear = lambda:os.system("cls")
cwd = os.getcwd()
container = Contacts()

def fileopen(path):
    try:
        with open(os.path.join(cwd, path), "r",encoding="utf-8") as data:
            text = data.readlines()
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
                data.write(f"\n{elem.name}, {elem.number}, {elem.coment}")
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


def main():
    while True:
        clear()
        print("""1. Открыть файл
2. Сохранить файл
3. Добавить контакт
4. Удалить контакт
5. Показать все контакты
6. Показать контакт
7. Остановить программу
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
                break

if __name__ == "__main__":
    main()
