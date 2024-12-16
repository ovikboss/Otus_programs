import pytest
from main import container, data_manager, cwd
from models import Contact

@pytest.fixture
def path():
    return "text.txt"

@pytest.fixture
def delete_obj():
    return "Овик"


@pytest.fixture
def obj():
    return Contact("Овик", "89012737270", "крутой кодер")

def test_open(path, obj):
    data_manager.file_open(path, cwd, container)
    contact = container.lst[0]
    assert contact == obj


def test_close(path):
    data_manager.save_file(path, cwd, container)
    assert container.lst == []

def test_show_all(obj):
    con = container.show_all()
    assert con == obj

def test_show_one(obj):
    name = "Овик"
    con = container.show_con(name)
    assert con == obj

def test_new_contact(obj):
    container.new_contact()
    assert container.lst[0] == obj

def test_remove_con_false(obj):
    assert container.remove_con() == "Такого пользователя нет"

def test_remove_con_true(delete_obj, obj):
    container.lst.append(obj)
    assert f"Пользователь {delete_obj} удален" == container.remove_con()

def test_change_num():
    container.new_contact()
    print(container.change(id=3, param= "Номер"))
    assert container.lst[0].number == 123123

def test_change_name():
    print(container.change(id = 3,param = "Имя"))
    assert container.lst[0].name == "123123"

def test_change_comment():
    print(container.change(id  =  3, param = "Комментарий"))
    assert container.lst[0].coment == "123123"


if __name__ == "__main__":
    pytest.main()