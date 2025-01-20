import pytest
from models import Contact

@pytest.fixture
def path():
    """фикстура для пути"""
    return "text.txt"

@pytest.fixture
def delete_obj():
    """фикстура для проверки удаления пользователя"""
    return "Овик"


@pytest.fixture
def obj():
    """фикстура для проверки обьекта"""
    return Contact("Овик", "89012737270", "крутой кодер")