import json

version='1.0.0'

def create_config_unit():
    token=input('Введите token \n')
    secretkey=input('Введите secret-key \n')
    authtoken=input('Введите auth-token \n')
    groupid=input('Введите group-id\n')
    connectionString=input('Введите connectionString\n')

    
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

def read_config():
    # Writes a list as the argument into the file. 
    # If file doesn't exist it will be created.
    try:
        data=json.load(open('config.json'))
    except:
        data=create_config()
        with open('config.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)



def main():
    read_config()



# if __name__=='__main__':
#     main()
