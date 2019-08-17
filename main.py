from confighandler import readconfig
import json

if __name__ == '__main__': 
    configuration=readconfig()
    print('\n ******  Welcome to confighandler version: {}! File version: {}.  *****!\n'.format(configuration.softwareversion,configuration.fileversion))