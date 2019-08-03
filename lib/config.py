'''
    файлы name.py
    здесь показыаем что есть классы наследники от абстрактных. 
    Здесь Config наследник от IConfig. 
    т.е. метод def get_json_string(self) должен быть реализован
'''
import json
from .vkapi import VK_API
from .db import DB
from .Unit import unit

class Config():
    def __init__(self, source_convey_layer1):    
        self.version = '1.0.0'
        self.Develop = unit("Develop", source_convey_layer1)
        self.Production = unit("Production", source_convey_layer1) 


        