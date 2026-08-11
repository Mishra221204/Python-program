#  Data types in python

# 1. Numeric - int,float ,complex

#  integer  -quotes is not used
a=12
print(a)

b=22
c=12
print(b+c)

# float  - point value 
a=12.34
print(a)
print(type(a)) # check data types

b=12.4
c=25.66
print(b+c)
print(b/c)

# complex 
a1=complex(3,5)
print(a1)
print(type(a1))  # check data types

# 2. Sequence - string,list,tuple

# 1. string  - quote ke under value likha jata hai
a="shubham"
print(a)

a1="12"
print(a1)

a2="123"
b="144"
print(a2+b)
print(type(a2+b))  #  check data types


# 2. list  - used []
   
a=[12,34,56]
print(a)
print(type(a))  # check data types


# 3. tuple - used ()
a=(12,44,67,88,)
print(a)
print(type(a))  # check data types

# 3. dictionary 
dict={'name':'shubham','age':12,'addres':'saraideeh'}
print(dict)
print(type(dict))

# 4. set
set={12,34,"shubham",False}
print(set)
print(type(set))  # check data types


#  5.Boolean
bool=True
bool1=False
print(bool)
print(type(bool))

#  6. binary  - byte,bytearray,memoryview
bytes=b"Madhav"
print(bytes)
print(type(bytes))