# String in python

#  3 type quote used

# 1. single Quote ('')
#  2. double Quote("")
#   3. triple Quote(''')



#  1 . single Quote
name=('shubham')
print(name)
print(type(name))    # check dta types 


# 2 . Double Quote
value=("My name is Shubham")
print(value)


# 3 . Triple Quote
#  truple quote hmm lgte hai to any quote used kr skte hai not proble

detail=('''My name is " shubham" and  you are king "function" ''')
print(detail)

print("  \"Kw - double Quote \" ")




#  Formatting string

#  Multi type insert variable in string
# 1. Old style formatting(% operator)  like c-language used
# 2. str.format () method
# 3. f string (formatting string)


#  1. Old style formatting(% operator)
#  (%) modular used krna jruri hai

name="shubham"
print("  my name %s"%(name))


name="shivam Mishra"
age=12
city="jaunpur"
print("My name is %s  I am %d from %s"%(name,age,city))


# 2. str.formate () method
# synatx- "string {}".format(value)
#  format() method is more powerful and flexible than the old-style % formatting


name="Shubham"
age=19
print("My name is {}  I am {}".format(name,age))


#  you can reference  by index or keyword
print("My name is {0}  I am {1}".format(name,age))
print("My name is {1}  I am {0}".format(name,age))  # index to change value bhi change


#  direct print not used varible  exter
print("my name is {name} I am {age}".format(name="Madhva",age=13))



#  3. F- string 

name="shubham mishra"
age=20
city="jaunpur"

print("My name {name} I am {age}  from {city}")  # f -sting not used " output not"
print(f"My name {name} I am {age}  from {city}")
print(f" My age after 5 year will be {age+5}")


# Ecape charactore
#  in special charactor is used in string 



# Escape characters  denoted by (\)

print(''' "Kw-double Quote" ''')

print(" \" hello shubham \" ")  # double quotes using backspce \

print(" \' hello shubham \' ")  # single quote using backspace \

print("Hello\nWorld")  # new line used (\n)

print("Hello\tWorld")  # tab- space hoga 



#  String Opeator in python
# 1. add
a= "Hello"
b="World"
print(a+b)  # add string

#  2. Multiply

print(a*b)  # multiply string not hoga
print(a*2)  # multiple hoga a*a
print(a*b)  # multiply string


#  [] - slice,[]-rang -- scroll bello



# 3. in - Member : return true if a chara exist given string

if "e" in a:
    print("yes")

else:
    print("No")    


# 4. not in - Membership : return true if a chara does not exist given string
#  not in used reverse true hai to false , false hai to true
if "e" not in a:
    print("yes")

else:
    print("No")     



 # 4.  Row string - suppress  actual meaning the escape chars

#  r used in quote ke under vale all print any function 
print("Hello\n world") 
print(r"Hello\n world")   # Row string - suppress the escape chars


# 5. (%)- format performa string formatting  

name="shubham"
age=12
print("my name is %s I am %d"%(name,age))


