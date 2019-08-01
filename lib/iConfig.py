""""
    Файлы  iName.py содержат абстрактные классы. 
    В классах описываем методы и свойства для реализации
"""
from abc import ABC, abstractmethod

class IConfig(ABC):

    @abstractmethod # означает что метод должен быть реализован в классе наследнике
    def get_json_string(self)->str:
        pass