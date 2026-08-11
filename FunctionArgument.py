# Function Argument in python

#  1. Requred Argument -(Single/Multiple Argument)

# single Argument
# def greting("madhav"):   # madhav is argument
#    greting()            # requride an argument to run code


# def greeting(name):  
#     print("Hello ",name,"!")
 
# call function
# greeting("shubham") 


#  Multilpy Argument
# def detail(name,age,addres,percentage):
#     print(f"My name {name}  I am {age} year old   From {addres}  and 12th percentage is {percentage}%!")

# call function
# detail("Shubham Mishra",20,"Saraydeeh Marikpur Jaunpur",72)


# 2 . default Argument
# def greeting(name="Madhav"):   # "madhav" is a  default value
#     print("Hello ",name,"!")

# greeting()      # runs with using default value
# greeting("Shubham")  


# def detail(name="Madhav",age=20,addres="Saraydeeh Marikpur Jaunpur",percentage=72):
#     print(f"My name {name}  I am {age} year old   From {addres}  and 12th percentage is {percentage}%!")


# detail()      # runs with using default value    
# detail("Shubham Mishra",20,"Saraydeeh Marikpur Jaunpur",72)   #  change value of default argument

# def value(a=10,b=20):
#       print("value of a is ",a ,"and value of b is ",b)
  
# value()      # runs with using default value   
# value(30,40)   #  change value of default argument


#  keyword Argument
# def detail(name,age,addres,percentage):
#     print(f"My name {name}  I am {age} year old   From {addres}  and 12th percentage is {percentage}%!")

#  call function
# detail("shuam",12,"saraideeh",72)


def math(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
    print(f"Subtraction of {a} and {b} is {a-b}")
    print(f"Multiplication of {a} and {b} is {a*b}")
    print(f"Division of {a} and {b} is {a/b}")  


# call function
math(b=20,a=10)       # keyword argument


#  Q 2-
def cal(a,b):
    return a/b

value= cal(a=20,b=10)
print(value)  



# Arbitrary Positional Arguments (*args)

def add2number(a,b):
    return  a+b

result=add2number(12,13)
print(result)                                 

# add 3 number

def add3number(a,b,c):
    return  a+b+c

result=add3number(12,13,12)
print(result)                                 

#  kb tak aise krte rhe ge used (*agr)

def Math(*arg):     #  multiply parmeter pass used (*arg)
    print(type(arg))  # data tpes check
    return sum(arg)

result=Math(12,12,12,3)    # multiply value  pass
print(result)
print(type(result))   # data types check value kon sa hai 

#  string pass 

def greeting(*names):
    for name in names:
        print(f"hello {name} ! ")

greeting("shubham","shivam","neha","satyam")



def  table(*num):
    print(" 1 to 10 table")
    for tab in num:
        print(tab)


table(1,2,3,4,5,6,7,8,9,10)        




# Arbitrary keyword Argument (**kwarg)
#  key and value ko dala jata hai
#  Note - store argument as dictory
def print_detail(**kwarg):
    for key ,value in kwarg.items():
        print(f"{key}: {value}")

print_detail(name="shubham",age=20,city="Jaunpur")



def detail(**value):
    for key,value in value.items():
        print(f" Hello {key}:{value} ")
detail(name="Madhva" , age=10,Addres="madhura", statu="ok")



#  10 name , age and address print
def function(**kwarg):
    for key,value in kwarg.items():
        print(f" {key} : {value} ")

# call function
 
function(name="shubha",age=20,Addres="saraideeh , Marikpur, Jaunpur")       

function(name="shivam",age=21,Addres="Basupur , Marikpur, Jaunpur")
       
function(name="satyam",age=23,Addres="saraideeh , Marikpur, Jaunpur")
       
function(name="Ankit",age=10,Addres="saraideeh , Marikpur, Jaunpur"
         )       
function(name="Naha",age=12,Addres="saraideeh , Marikpur, Jaunpur")

function(name="Pari",age=15,Addres="saraideeh , Marikpur, Jaunpur") 

function(name="Nandni",age=18,Addres="saraideeh , Marikpur, Jaunpur")

function(name="shubha",age=20,Addres="saraideeh , Marikpur, Jaunpur"
         )       
function(name="Rakesh",age=30,Addres="saraideeh , Marikpur, Jaunpur")

function(name="Santosh",age=28,Addres="saraideeh , Marikpur, Jaunpur")       