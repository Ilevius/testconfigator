import json
from random import choice

version='1.0.0'

def create_config_unit():
    token=''
    secretkey=''
    authtoken=''
    groupid=''
    connectionString=''

    numletters=['a','b','c','1','2','3']

    while len(token) !=5:
        token+=choice(numletters)
        secretkey+=choice(numletters)
        authtoken+=choice(numletters)
        groupid+=choice(numletters)
        connectionString+=choice(numletters)
    
    vkapi={
        'token': token,
        'secret-key': secretkey,
        'auth-token': authtoken,
        'group-id': groupid
    }

    database={
        'connectionString': connectionString
    }

    config_unit={   
        'vkapi': vkapi,
        'database': database
    }

    return config_unit

def create_config():
    config={
        'version':version,
        'Production':create_config_unit(),
        'Develop':create_config_unit()
    }
    return config

def write_json(person_dict):# Writes a list as the argument into the file. If file doesn't exist it will be created.
    try:
        data=json.load(open('config.json'))
    except:
        data=create_config()
        with open('config.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)



def main():
    write_json(create_config())



if __name__=='__main__':
    main()
