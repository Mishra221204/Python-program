# Dictionary in python

#  syntax :-
# my_dict ={'key1':'value1','key2':'value2',....}

# Method-1 :- create dictionary using curly braces

detail={'couse':'Python',
        'Instructor':'Rishabh Mishra',
        'Name':'Shubham Mishra'}
print(detail)
print(type(detail))


# Method- 2 :- dict()  Constructor

person=dict(name='shubham',age=13,grad='A')
print(person)
print(type(person))


#  Method-3 :- Using list of tuple

detail=dict([('name','shubham'),('age',20),('city','Mathura')])
print(detail)
print(type(detail))

detail1=(('name','shubhm'),('age',12))
print(detail1)
print(type(detail1))

detail2=dict(detail1)   # tuple convert to dict
print(detail2)



#  Access dictionary values

student={
    1:'class-X',
    'name':'Shubham Mishra',
    'age':20,
    'grade':'A',
    'city':'Jaunpur'
}

print(student)   
print(type(student))    # check data types

#  Name is access
print(student['name'])     #output- shubham Mishra
print(student['age'])    # output-20
print(student['grade'])   # output -A



#  dictionar Method
#  Python provides several  built in Method  
# to use on dictionary



#  Dictionary Method
#  Here are a few  useful methods

#  . key() - Return all keys in the dictionary
#  . value() - Return all value in the dictionary
#  . items() - Return all key- value pairs
#  . get()  -  Return value for a key(with an optional default if key missing)



student={
    1:'class-X',
    'name':'Shubham Mishra',
    'age':20,
    'grade':'A',
    'city':'Jaunpur'
}


#  key() access

print(student.keys())       # all keys

#  value() acess

print(student.values())    # all value

#  .items()  acess

print(student.items())   # key - value pair


#  . get()  access

print(student.get('name'))     #  pass name 
print(student.get('age'))       #  access  age




#  Dictionary -  Add , Modify  & Remove Items




student={
    1:'class-X',
    'name':'Shubham Mishra',
    'age':20,
    'grade':'A',
    'city':'Jaunpur'
}


#  1. Add or Modify item : use assign- opertor '=' to add/modify item in a dictionary

#  Adding a new  key- value pair

student["email"]="mishrashubham7636@gmail.com"    # add
print(student)


student["addres"] = "saraideeh"
print(student)


#  Modify on exist value

student['name']="shivam"
print(student)

student['age']=15
print(student)



#  Remove Item - use  del or pop() to remove item form a dictionary


#  Remove with del

del student['age']   # remove
print(student)


#  Remove with pop() and store the removed value
#  value output

city=student.pop('city')
print(city)




#  Dictionary iterations
#  A dictionary can be iterated  using for loop we can loop through dictionaries by keys, values, or both

student={
    1:'class-X',
    'name':'Shubham Mishra',
    'age':20,
    'grade':'A',
    'city':'Jaunpur'
}



#  Loop through keys
for key in student:
    print(key)   # key output


# Loop through value

for value in student:
    print(student[value])


#  Loop through value : using value() method

for value in student.values():
    print(value)


#  Loop through both keys and values
for key,value in student.items():
    print(key,value)



#  Nested Dictionary
#  Dictionaries can cantain other dictionarires which is useful for storing more complex data

student={
"student1":{
    1:'class-X',
    'name':'Shubham Mishra',
    'age':20,
    'grade':'A',
    'city':'Jaunpur'
},
"student2":{
    "name": "Shivam",
    "age": 21,
    "grade":"B"
}
}


#  access value

print(student['student1']['name'])    # output : Shubham 

print(student['student2']['age'])



main_student={

    'student1':{'name':'shubham','age':20},
    'student2':{'name':'shivam','age':22}
}

# #  access value

print(main_student['student1']['name'])
print(main_student['student2']['age'])




#  Dictionary Comprehension
#  A dictionary comprehension allow you to creat dictionaries in a 
# concise way

# Syntax -

# new_dict =
# { key_expression : value_pression for item iterable if condtion }


square={x:x *x for x in  range(1,6)}
print(square)


student={'name':'Shubham','age':23,'city':'saraideeh'}

key={key for key  in student.keys()}    # key acess
print(key)


value={value for value  in student.values()}    # vale acess
print(value)

key_value={key : value for key, value  in student.items()}    # both acess 
print(key_value)