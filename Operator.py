#  Operator in python

# 1. Arthmetic operator
a=5
b=10
print(a+b)  # addition operator
print(a-b)  # substraction operator
print(a*b)  # multiply operator
print(a%b)  # modulare operator


# 2.Comparison (Relation )  Operator

a=10
b=10
print(a==b)  # equal to 
print(a!=b)  # not equal to 

a1=10
b1=5
print(a1>b1)  # greater than
print(a1<b1)   # less than 
print(a1>=b1)  # greater than equal
print(a1<=b1)   # less  than equal


# 3. Assigment operator
a=5 


# 4. Logical operator
#  Rule  used for  and 
# 1. True + True =True
# 2. True + false = false
# 3. False + false = false 


a=10
b=10
print(a>10 and b<10)  # and operator   two side true  return true but not true return not true


#  Rule  used for  (or) 
# 2. True + false = True
 
print(a>10 or b<10)   # or operator one side true is return true
print(a==10 and b==20)

# Rule for 'not' 
# Ture  reverse = false
#  False reverse to = True

a=10
b=20
print(not (a==10 and b==20))



#  5. Identity operator - is, is not
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)  # is operator  same merory location
print(x is z)  #  value same but varibale different

#  reverseing  {true hai to false}
print( x is not z)  # ture value


# Membership Operator  - in , in not
#  truple, string, list

my_list=['mango', 'apple','banan', 'graps']
print('apple' in  my_list)   # in operato
print('banan' in  my_list) 
print('papap' in  my_list)  # not preset my_list

#  reverse ' in not'
# print('papap' not in my_list) 



#  7 . Bitwise operator -  AND-(&),OR-(|),XOR-(^),NOT-(~) ETC\

a=5   # 5 in binary - 0101
b=3   # 3 in binary - 0011
print(a&b) #  1 in binary - 0001

#  Rule  used for  and  & operator 
# 1. True + True =True
# 2. True + false = false
# 3. False + false = false

a1=5  # 5 in binary - 0101
b1=8  # 8 in binary - 1000
            
print(a1 & b1)   