from lib.config import Config
import json

if __name__ == '__main__':
    configfile=open("config.json", mode='r')
    configcontent=json.load(configfile)
    conf = Config(configcontent)
    
    print('\n ******Next step*****!\n')
    print(conf.Develop.db.connection_string)
    print(conf.Develop.vkapi.token)
    print(conf.Production.db.connection_string)