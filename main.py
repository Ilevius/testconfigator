from lib.config import Config
import json

if __name__ == '__main__':
    print('Run!')
    conf = Config()
    print(conf.get_json_string())

    print('\n ******Next step*****!\n')
    configfile=open("config.json", mode='r')
    configcontent=json.load(configfile)
    print(configcontent)