#  Tuple in Python 
#  used in  parenthesis()- main important used (,) 
#  issse pta chalta hai ki tuple hai


my_tuple=("Shubham","Shivam","Satyam","Neha")
print(my_tuple)
print(type(my_tuple))   # check data types


#  Without parenthesis
tuple=1,2,3,4
print(tuple)
print(type(tuple))

#  tuple constructor
tuple1=tuple((12,22,44,55))
print(tuple1)


# list convert to tuple

list=[1,2,3,4]
new_tuple= tuple((list))     # convert 
print(new_tuple)


# creat a single element -  single element  danger hote hai

#  parentheise used hoga aur double quote bhi 
#  but vo string rhe ga used krna padhe ga commal(,)

a=("a",)     # commma add

print(type(a))



#  differ data types used 

my_truple1=("Shubham","Shivam",1,2,3,23,True,3.12,3.14)

print(my_truple1)

#  do not change in tuple
my_truple1[1]="satyam"
print(my_truple1)   # not change




#  Tuple in index no access
# Positive  - (start 0 in any number) 
# & negtive  - (last no 1 to first any number)

my_truple1=("Shubham","Shivam",1,2,3,23,True,3.12,3.14)


#  access  positive index
print(my_truple1[1])    # output-shivamg
print(my_truple1[3])   # output- 2


#  access negative index
print(my_truple1[-1])   # output - last 3.14 print
print(my_truple1[-9])   # output - first shubham print



#  Slicing in Truple
# syntax- [start : end : step]

my_truple1=("Shubham","Shivam",1,2,3,23,True,3.12,3.14)

print(my_truple1[0:6])    # [ start : end ]

print(my_truple1[0:6:1])   # [ start : end : step]

print(my_truple1[0:6:2])

#  negative index

print(my_truple1[-6:-1])    # [ start : end]

print(my_truple1[-6:-1: 2])  # [ start : end : step]


#  print first to last value
print(my_truple1[0:-1])




#  Tuple Operationsd

#  Q1. Concatenation
#  you can join two or more tuple using + operator


tuple=[12,22,33,44]
tuple1=[11,12,22]

combined=tuple1+tuple  # + operator used
print(combined)


#  Q2. Repetition
#  You can repeat a tuple multiple time using the * operator

tuple3=("hello",) *4      # * operator used
print(tuple3)




#  checking for an item
#  use the in keyword to check if an item exists in a tuple 

number=(20,30,40,20)
print(20 in number)     # True  

print (30 in number)





#  iterating over tuple
#  iterating allows you to traverse each element in a tupe using loop


# Q1. using for loop

fruits=("apple","Banana","Mango","cherry")

for i in fruits:
    print(i)



# Q2 .   using while loop

i=0

while i<len (fruits):
    print(fruits[i])
    i+=1   


# Q2-

number=(12,22,33,44,455)

j=0

while j <len(number):
    print(number[j])

    j+=1 



#  Tuple Method
#  python provides two built in- methods to using on tuple

#  1- count

color=("red","Pink","yellow","blue","red")

print(color.count("red"))    # output 2
print(color.count("Pink"))


#  2- index

print(color.index("blue"))    # 3

print(color.index("red"))




#  Tuple in function
#  python provides two built in- methods to using on tuple


#  1. len()
#  return the number of item in a tuple

number=(12,22,33,44,455)
print(len(number))


#  2. sorted()
#  Return a new sorted list from the item in the tuple

sorted_num= sorted(number)   # convert truple to list
print(sorted_num)


#  3. sum()
# sum the sum in tuple 

number=(12,22,33,44,455)
print(sum(number)) 



#  min(),max()
#  min()- return sallest number
#  max()- return largest number

number=(12,2,22,12,33)

print(min(number))   # output - 2

print(max(number))  #  output- 33




#  Packing and Unpaking Tuple

# a. "packing"- is the process of putting multiple value into a single tuple

a="Madhav"
b=21
c="engineer"

pack_tuple=a,b,c   # packing value into a tuple
print(pack_tuple)


#  b. "Unpacking"- is extracting the value form a tuple into separat
#  jitne value hai utna variable bhi hoga  exter variable loge to error aaye ga

name , age,profession = pack_tuple

print("Name is ",name)
print("age",age)
print("Profession",profession)



#  Modifying Tuple - Immutable
#  Once a tuple is created you cannot modify ist element this means you 
#  cannot add,remove or change


#  creating a tuple

number=(1,2,3,4)

#  Attempting to change an item

number[2]=12
print(number)  # erro

#  how to mutate / modify tuple

#  tuple convert to list  and list modify/change to element
number=(1,2,3,4)
number1=list(number)   # convert to list 
print(number1)

number1[1]=20    # Modify element
print(number1)

#  List convert to tuple
tuple_number=tuple(number1)   # convert 
print(tuple_number)




#  Q1 - Modify , add, remove etc method  used in tuple

Tuple_number=(12,22,44,55,66,13,44)

# Modify 

list_number=list(Tuple_number)
# print(type(list_number))   # convert to list

list_number[3]=25
print(list_number)


list_number[2]="shubham"
print(list_number)


#  Add element -(append)

list_number.append(12)
print(list_number)

list_number.append("satyam")
print(list_number)


#  Remove the element

list_number.remove(13)
print(list_number)   # output remove 13
print(list_number)


#  List convert to Tuple

Tuple_number1=tuple(list_number)   # convert to tuple
print(Tuple_number1)