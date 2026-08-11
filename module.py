#Module in python
#  Single py file


#  create a module mymodule.py file

#  use mymodule file
# import mymodule
# mymodule.say_hello('Madhav',20)
# mymodule.say_bye('shubham')


#  import/use specific part of code   
#  used (from)

from mymodule import person
print(person)

from mymodule import person3
print(person3)


#  package :- collection  modules/.py file  ke under ( __init__.py) hoga 
#  to usse package khte hai nhi hoga __init__.py to usse 'module khte hai'
#  multiple file hoga 


#  Library :- collection of modules and packages

#   in- built libray
import math   # math library used to calculation 
a=36
print(math.sqrt(a))

b=12
print(math.sin(b))


#  import specific function from libarary

from math import factorial
c=6
print(factorial(c))


#  installed new modules/lib
# kisi bhi libray ko installed kre ke 
#  liye used (pip  library name) 


# pip install<libray_name  
# import pandas in pd

