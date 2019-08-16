from confighandler import config
import json

if __name__ == '__main__':
    configfile=open("config.json", mode='r')
    configcontent=json.load(configfile)
    configfile.close()
    conf = config(configcontent)
    print('\n ******  Welcome to confighandler version: {}! File version: {}.  *****!\n'.format(conf.softwareversion,conf.fileversion))