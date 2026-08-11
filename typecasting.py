#  Type casting in python - 2 types implicit and explicit
#  comverting a value from one data types in another data types
#  int(),float(),bool(),set(),dict()

a="12"
b=12
c=int(a)  # type casting
print(c+b)


a1=12.34
b1=1245

print(a1+ float(b1))   # int convert to float



a=12      # int convert to str
b="123"

print(str(a)+b)

#  all str type can't be casting into numerical type
name="shubham" 
print(int(name))  # not change 


f1=12.25
print(type(int(f1)))   # float value convert to int


b1=1
print(bool(b1))

b=0
print( float(b))  # int value convert to float

print(bool(b))  # int value convert to bool


s='shubham '
print(set(s))  # str value convert to set

s1=12345
print(set(s1))  # not convert



a=12
print(complex(a))   # int value convert to complex

b='shubham'
print(complex(b))  # str value not convert comples


c=12
print(bin(c))  # int value convert to binary



#1. Implicit types casting from integer to flaot
num_int=123
num_float=12.2

result=num_int+num_float
print(result)
print(type(result))


# 2.explicit types casting
int_num=123
result=str(int_num)
print(type(result))


a1=bool(1)
print(a1)
print(type(a1))

a0=bool(0)
print(a0)
print(type(a0))