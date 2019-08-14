'''
    Экземпляр сего класса при создании создаёт два класса среднего уровня
    и пишет их себе в поля. Принимая аргумент при инициации он передает его
    средним классам при их создании.
'''
import json
from .Unit import unit

class Config():
    def __init__(self, source_convey_layer1):    
        self.version = '1.0.0'
        self.Develop = unit("Develop", source_convey_layer1)
        self.Production = unit("Production", source_convey_layer1) 


        