import os
from models import  Contacts_Collection
from controller import Data_file

clear = lambda:os.system("cls")
cwd = os.getcwd()
container = Contacts_Collection()
data_manager = Data_file()


def main() -> None:
    """Основная программа"""
    var = ""
    while var != 8:
        #clear()
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
                    container.new_contact()
                    input("что бы продолжить введите любой символ")
                case 4:
                    container.remove_con()
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
