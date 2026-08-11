#  Condition Statement in python


# 1. if statement
#  if satatement works only for true condition

a=200
b=208

if b>a:
   print("b is greter than")

age= int(input("enter your age"))

if age>19:
   print(" You are adoult")



# 2 . if else condition 
#   work true and false dono 

a=12
b=10

if a>b:
   print("a is greater than")

else:
   print("b is greater than")


# ex 
age=int(input("enter your age"))

if age>18:
    print("You are vote")

else:
   print("You are not vote")    




#  3.  if - elif-else statement
# multiply condition

marks=int(input("enter marks "))

if marks>=90:
    print("top ranks")

elif marks>=80 :
     print("secand top")

elif marks>=60:
     print("third ranks")     

else:
     print("third division")     


#  4. Nested if-else statement
#  if-else inside if-else statement
#  multiply condition depend on each other

# Q  positive , negative & zero . positive - even/odd

number=int(input("enter a number"))

if number>0:
    if number %2==0:
        print("this is even number")
    else:
        print("this is odd number")
else:
    if number==0:
        print("this is zero")
    else:
     print("this is negative")
                  

# Q2 -

number=int(input("enter a number"))

if number %2==0:
    print("this is even number")

else:
    print("this is odd no")


# 5. conditional expression (ternary operator)

age=16
status="Major" if age>=18 else "Minnor"   
print(status)

