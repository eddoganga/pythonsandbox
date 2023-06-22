# dictionaries collection of unordered, changeable and indexed. no duplicate

#create a dict

person = {
    'first_name': 'eddwoj',
    'last_name': 'omosh',
    'age': 39
}


#get value

print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '555-55-5555-55'

#get dict keys

print(person.keys())

#get dict items
print(person.items())

#copy dict

person2= person.copy()
person2['city'] = 'kisumu'

print(person2)

print(person)