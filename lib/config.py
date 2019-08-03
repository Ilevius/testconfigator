'''
    файлы name.py
    здесь показыаем что есть классы наследники от абстрактных. 
    Здесь Config наследник от IConfig. 
    т.е. метод def get_json_string(self) должен быть реализован
'''
import json
from .iConfig import IConfig
from .vkapi import VK_API
from .db import DB
from .Unit import unit

class Config(IConfig):
    def __init__(self, configcontent)    
        self.version = '1.0.0'
        self.Develop = unit("Develop", configcontent)
        self.Production = unit("Production", configcontent) 
    _vk_api =  VK_API('').get_json()
    _database  =  DB('').get_json()
    config = {
        'version':version ,
        'vk_api': _vk_api,
        'database':_database
    }    
        
    def get_json_string(self):        
        return json.dumps(self.config)    


        