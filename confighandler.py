import json
from random import choice


def gen_person():
    name=''
    tel=''
    letters=['a','b','c']
    nums=['1','2','3']

    while len(name) !=5
       name+=choice(letters)
       tel+=choice(nums)
    
    person={
        'name'=name,
        'tel'=tel
    }

    return person

def write_person(person_dict):
    try:
        data=json.load(open('persons.json'))
    except:
        data=[]
    data.append(person_dict)

    with open('persons.json', 'w') as file:
        json.dump(data, file, indent, ensure_ascii=False)











def main():
    persons=[]
    for i in range(5):
        write_json(gen_person())



if __name__=='__main__':
    main()
