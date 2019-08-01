import json
from random import choice


def create_config():
    token=''
    secret-key=''
    auth-token=''
    group-id=''
    connectionString=''
    version='1.0.0'

    numletters=['a','b','c','1','2','3']

    while len(name) !=5:
        token+=choice(numletters)
        secret-key+=choice(numletters)
        auth-token+=choice(numletters)
        group-id+=choice(numletters)
        connectionString+=choice(numletters)
    
    vkapi={
        'token': token,
        'secret-key': secret-key,
        'auth-token': auth-token,
        'group-id': group-id
    }

    database={
        'connectionString': connectionString
    }

    config={
        'version': version,   
        'vkapi': vkapi,
        'database': database
    }


    return person

def write_json(person_dict):# Writes a list as the argument into the file. If file doesn't exist it will be created.
    try:
        data=json.load(open('persons.json'))
    except:
        data=[]
    data.append(person_dict)

    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)









def main():
    persons=[]
    for i in range(5):
        write_json(create_config())



if __name__=='__main__':
    main()
