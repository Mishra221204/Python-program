# # python program to create a single calculator

# # 3 step to build in calculator
# # 1. function for operation
# # 2. user input
# # 3. print result

# #  function to add two number
def Add(num1,num2):
    return num1+num2


# #  function to substract two number
def substract(num1,num2):
    return num1-num2


# #  function to multiply two number
def multiply(num1,num2):
    return num1*num2


#  #  function to divide two number
def divide(num1,num2):
    return num1/num2

#  function to multiply two number
def avg(num1,num2):
    return (num1+num2)/2


#  2 user input
print(" Select the option: \n"\
      "1. Addition \n"\
      "2. Substraction \n"\
      "3. Multiplication \n"\
       "4. Dividion \n"\
        "5. Average " )

select=int(input("Select a operation from 1,2,3,4,5:"))

number1=int(input("enter a first number:"))
number2=int(input("enter a secand number:"))

#  print result 

if select==1:
    print(number1, "+", number2,"=", \
          Add(number1,number2))
elif select==2:
    print(number1,"-",number2,"=",\
         substract(number1,number2) )

elif select==3:
    print(number1,"*",number2,"=",\
         substract(number1,number2) )
    
elif select==4:
    print(number1,"/",number2,"=",\
         substract(number1,number2) )
 
elif select==5:
    print("(",number1,"+",number2,")","/","2","=",\
          avg(number1,number2))
    

else:
    print("Invalid value chose")   


#  Mini num project 3 number calculator

#  function
def multiply(num1,num2,num3):
    return num1*num2*num3

def substract(num1,num2,num3):
    return num1-num2-num3

def Add(num1,num2,num3):
    return num1+num2+num3

def modular(num1,num2,num3):
    return num1%num2%num3

def avg(num1,num2,num3):
    return (num1+num2+num3)/2


#  select input
print(" Select the option:\n"\
           "1.  Multtication the number \n"\
            "2. sub no \n"\
             "3. Add to number\n"\
            "4. Modulare number\n"\
            "5. Average number" )

select=int(input(" Enter a option from 1,2,3,4:"))

number1=int(input(" Enter the first number:"))
number2=int(input("enter the secand number:"))
number3=int(input(" enter the third number:"))
# print
if select==1:
    print(number1, "*", number2,"*",number3,"=",\
       multiply(number1,number2,number3))
elif select==2:
    print(number1,"-",number2,"-",number3,"=",\
          substract(number1,number2,number3))  

elif select==3:
    print(number1,"+",number2,"+",number3,"=",\
          Add(number1,number2,number3))  

elif select==4:
    print(number1,"%",number2,"%",number3,"=",\
          modular(number1,number2,number3))     


elif select==5:
    print("(",number1,"+",number2,"+",number3,")","/","2","=",\
            avg(number1,number2,number3))



else:
    print("Invalide option choes")     
