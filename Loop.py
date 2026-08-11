#  Loop in python -while & for loop

#  While loop  - True value

#  1 to 4 print number  Accending order

count=0
while count<=4:   # condition
    print(count)
    count +=1


#  1 to 20 number print

count=1
while count<=20:
    print(count)
    count+=1



#  2 to 20 table  print
value=2

while value<=20:
    print(value)
    value+=2 




#  4th table print
count=4

while count<=40:
    print(count)
    count+=4 



#  Decending order 5 to 1

value=5

while value>=0:
    print(value)
    value-=1


#  else bhi used kr skte hai false

#  Decending order 5 to 1

value=5

while value>=0:
    print(value)
    value-=1
else:
   print(" While loop end")


#  inifinet loop nhi krna hai 

while   True :
    print(" Hello Shubham")





#  For loop 

#  iterat  over each character in language

language="python"   # sequence

for x in  language:
    print(x)


#  Range function used same slicing

range(start,stop,step)
range(stop)      # single value boge to stop lega


#  1 to 5 print in for loop

for i in range(6):  # range(stop)
    print(i)


for y in range(1,11):   # range (start,step)
    print(y)    


for z in range(2,21,2):   # range (start,step,step)
    print(z)    

else:
    print("for loop ended")
        


#  Loop control statement - allow to alter a normal flow loop 

#  python support 3 clouse 

#  1- pass statement
#  2- break statement
#  3- continues statement


#  1- pass statement
#  pass used code not error future used

count=5
while count>=0:
    if count==3:
        pass     # pass statement 
    else:
        print(count)
    count -=1     


#   break statement - terminates the loop entirely existing from it 
#  immediately 


for i in range(5):
    if i==3:
        break   # break statement
    print(i) 


#  Continues  statement 

for i in range(10):
    if i==5:
        continue   # continues statement
    print(i)



#  different b/w pass / continues

#  yh chala gya infinite loop me  continues used 
count=5
while count>=0:
    if count==3:
       continue  
    else:
        print(count)
    count -=1     


while True:
    user_input=input(" Enter a 'exist' to 'stop' ")
    if user_input=='exist':
        print(" Congurate ")
        break
    print("sorry you enter rong", user_input)





#  Nested loop in python  - loop inside another loop
# outer loop - one time run kre gade 
#  inner loop  - run all iteration  run 


#  syntax-
#  outer_loop :
    #  inner_loop :
           #block of code for inner code

# block of code for outer code  


#  print number 1 to 4  in 3 time

for i in range(4):   # outer loop
    for num in range(1,5):   # inner loop
     print(num)
    print("-----") 


#  print form 1 to 3 for 3 time using while-for loop :
# nested loop

count=1
while count<4:
   print("while loop iteration no".count)  
   for i in range (1,4):
      print(i)
    #   print("----")
      count +=1 


#  print  prime number b/w range 2 to 10 using nested loop

for num in range(2,10):
    for i in range(2,num):
        if num % i== 0:
         break
    else:
       print(num)   


#   print a prime number 

user=int(input("enter a number"))

if user % 2==0:
    print("It is prime number")

else:
    print("it is not prime number")    

