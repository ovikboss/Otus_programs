class NotValidInput(Exception):
    """Не правильный ввод данных"""
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = None
    
    def __str__(self):
        if self.massage:
            return f"My exception: {self.massage}"
        else:
            return f"Пустое исключение"

class ErrorPathName(Exception):
    """Ошибки в названии пути файла"""

    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = None
    
    def __str__(self):
        if self.massage:
            return f"My exception: {self.massage}"
        else:
            return f"Пустое исключение"