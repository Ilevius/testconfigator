from lib.config import Config
import json

if __name__ == '__main__':
    configfile=open("config.json", mode='r')
    configcontent=json.load(configfile)
    configfile.close()
    conf = Config(configcontent)
    print('\n ******  Welcome to confighandler version: {}! File version: {}.  *****!\n'.format(conf.softwareversion,conf.fileversion))