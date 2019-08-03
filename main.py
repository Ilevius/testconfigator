from lib.config import Config
import json

if __name__ == '__main__':
    print('Run!')
    configfile=open("config.json", mode='r')
    configcontent=json.load(configfile)
    print('\n ******Next step*****!\n')
    
    conf = Config(configcontent)

    print(conf.Develop.db.connection_string)