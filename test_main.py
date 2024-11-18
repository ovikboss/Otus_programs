import pytest
from main import container, data_manager, cwd
from models import Contact

@pytest.fixture
def path():
    return "text.txt"

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


if __name__ == "__main__":
    pytest.main()