import json
from random import choice

version='1.0.0'

def create_config_unit():
    token=''
    secret-key=''
    auth-token=''
    group-id=''
    connectionString=''

    numletters=['a','b','c','1','2','3']

    while len(name) !=5:
        token+=choice(numletters)
        secret-key+=choice(numletters)
        auth-token+=choice(numletters)
        groupid+=choice(numletters)
        connectionString+=choice(numletters)
    
    vkapi={
        'token': token,
        'secret-key': secret-key,
        'auth-token': auth-token,
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
    persons=[]
    for i in range(5):
        write_json(create_config())



if __name__=='__main__':
    main()
