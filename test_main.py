import pytest
from main import container, data_manager, cwd

from conftest import path, delete_obj, obj



def test_open(path, obj):
    """Тест открытия файла"""
    data_manager.file_open(path, cwd, container)
    contact = container.lst[0]
    assert contact == obj


def test_close(path):
    """Тест закрытия файла"""
    data_manager.save_file(path, cwd, container)
    assert container.lst == []

def test_show_all(obj):
    """тест показа данных"""
    con = container.show_all()
    assert con == obj

def test_show_one(obj):
    """тест показа конкретного пользователдя"""
    name = "Овик"
    con = container.show_con(name)
    assert con == obj

def test_new_contact(obj):
    """тест создания нового пользователя"""
    container.new_contact()
    assert container.lst[0] == obj

def test_remove_con_false(obj):
    """тест неудачного удаления пользователя"""
    assert container.remove_con() == "Такого пользователя нет"

def test_remove_con_true(delete_obj, obj):
    """тест удачного удаления пользователя"""
    container.lst.append(obj)
    assert f"Пользователь {delete_obj} удален" == container.remove_con()

def test_change_num():
    """тест изменений данных"""
    container.new_contact()
    print(container.change(id=3, param= "Номер"))
    assert container.lst[0].number == 123123

def test_change_name():
    """тест изменений данных"""
    print(container.change(id = 3,param = "Имя"))
    assert container.lst[0].name == "123123"

def test_change_comment():
    """тест изменений данных"""
    print(container.change(id  =  3, param = "Комментарий"))
    assert container.lst[0].coment == "123123"


if __name__ == "__main__":
    pytest.main()