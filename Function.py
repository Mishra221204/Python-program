# Function in python


#  creat function without  parameter
def greeting():
    print("heloo shubham ")

greeting() 
    
#  creat function using parameter

#   Add two number in function

def Add(a,b):      # function 
    result = a+b
    print(" the sum number:",result)  

Add(5,6)     # call function



#  Multiply two number in function

def multi(a,b):
    shubham = a*b
    print(" the multiply number:",shubham)  

#  call function
multi(5,6)   

#  change bhi kr skte hai diffine
multi(a=6,b=5) 




#  Add three number in function

def Add(a,b,c):      # function 
    result = a+b+c
    print(" the sum number:",result)  

Add(25,25,25)     # call function




#  Function with  return statement
def Addnum(a,b):
    return a+b

result=Addnum(4,7)
print(result)


#  function to convert celsiue to fahrenheit - without return 
def celsiue_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5) +32
    return fahrenheit

# call function   
tem_f=celsiue_to_fahrenheit(25)
print(tem_f)


#  different b/w  return and print

#  print jo Nonetype hota hai
# def celsiue_to_fahrenheit(celsius):
#     fahrenheit=(celsius*9/5) +32
#     print(fahrenheit)

# # call function   
# tem_f=celsiue_to_fahrenheit(25)
# print("without return",type(tem_f)) 

# #  return  value correct bata hai  'float'
# def celsiue_to_fahrenheit(celsius):
#     fahrenheit=(celsius*9/5) +32
#     return fahrenheit

# # # call function   
# tem_f1=celsiue_to_fahrenheit(25)
# print("without return",type(tem_f1))


# #  Pass statement
# def greeting():  # code to be update late


#   pass 
# print("hello")




#  Q 1- input add,multiply,divide, substraction ,modular


# Add
a0=int(input("enter number first"))
b0=int(input("enter a muber secand"))

c=a0+b0
print(" Sum the number",c)


# Multiply
#  input
 
a1=int(input("enter number first")) 
b1=int(input("enter a muber secand"))
result=a1+b1
print(" Multiply the number",result)


