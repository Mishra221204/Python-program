#  List in python


my_list=["shubham","shivam","satyam"]

print(my_list)
print(type(my_list))

#  mutiple  item in single variable
 
my_list1=[1,2,3, "Shubham",3.13,True]
print(my_list1)  
print(type(my_list1))  # check data types

#  Nested list
my_list2=[1,2,3,[ "Shubham","Shivam",[True],"satyam",],1,234,]

print(my_list2)



#  Access list - Indexing
#  positive - 0 to any
# & Nagative  - -1 end start to any number first

list=["shubham","shivam","Satyam"]
# index - 0,1,2,3,

print(list[2])   # access satyam
print(list[0])   # acess shubham


list1=[1,2,3,44,55]
print(list1[4])   

# Negative

list2=["shubham","shivam",12,34,55,66, True]
#  index- -7,-6,-5,-4,-3-,2,-1

#  True acces in negative
print(list2[-1])

#  shivam access in negative
print(list2[-6])



#  List Slicing
#  syntax - list_name[start : end : step]

value=[10,12,33,44,55,66]
print(value[0:4])   #  [start : end]
print(value[0:5:2])  # [ start : end : step]  
print(value[1:5:1])  # [start: end: step]

#  Negative index
value1=[12,22,44,33,35,44,56]
print(value1[-7:-3])   # [ start :end]

print(value1[-7:-2:1])  # [star: end: step]
print(value1[-7:-2:2])
print(value1[::-1])   # all value print
print(value1[-7::])   # start to end value print 



#  Modifying List - Add-append(),removing, changing

fruite=["Mango","grapes","banana","orange"]

#  Add  an element
fruite.append("papaya")
print(fruite)

fruite.append("blackberry")
print(fruite)

#  Changing  an element
fruite[2]="cherry"
print(fruite)

fruite[4]="shubham"
print(fruite)


#  remvoing an element
fruite.remove("blackberry")  # blackberry removing 
print(fruite)



fruite.remove("shubham")    # shubham removing
print(fruite)




#  List method

 # 1- append  method

fruits=["Apple","banana","grapes","Orange"]
fruits.append("Blackberry")
fruits.append(1.23)
print(fruits)


# 2 - extend  method
# two variable list  ko ke sath print  used extend 
fruits=["Apple","banana","grapes","Orange"]
more_fruits=["blackberry","papapy"]         # another list
fruits.extend(more_fruits)      # add fruits in more_fruits 
print(fruits)


num=[12,42,54,55,65]
num1=[1,2,4,6,8,]
num1.extend(num)   # print num1 me add num value used 
print(num1)



# 3 - insert   Method
#  index no se value ko dalna 

fruits=["Apple","banana","grapes","Orange"]
fruits.insert(1,"blackberry")                  # value ko index 1 per dalna
print(fruits)

#  index 3 value enter  - papaya
fruits.insert(3,"papaya")
print(fruits)




# 4  Remove method
#  revome the element in last 

fruits=["Apple","banana","grapes","Orange"]

fruits.remove("Orange")
print(fruits)


# 5- Clear method - is used list empty krna

fruits=["Apple","banana","grapes","Orange"]
fruits.clear()       # empty list
print(fruits)



# 6- Finding  index
#  kon sa element kon se index per hai

fruits=["Apple","banana","grapes","banana","blackberry","papaya","banana"]
index=fruits.index("banana")                      # new variable creat acces index
print(index) 

#  finding  index - with a range 
index1=fruits.index("banana",2)   # (element,step)
print(index1)


#  finding index- with range 3 ke bad
index2=fruits.index("banana",4)
print(index2)  # output 6



# 7 - count element
#  count element is used kitne time element aaya hai 

fruits=["Apple","banana","grapes","Orange","Apple","Orange"]
count=fruits.count("banana")
print(count)

count1=fruits.count("Orange")
print(count1)     # output 2 time Orange

count2=fruits.count("Apple")
print(count2)



# 8 -  Reverse List 
#  Element ko reverse krna

fruits=["Apple","banana","grapes","Orange"]

fruits.reverse()
print(fruits)




#  9 - Sorting List  - only numeric value
#  sort is used  assending order  

num=[12 , 22 , 1 , 22 , 43]
num.sort()    # default sort asc order
print(num)

number=[2,12,44,56,77,22]
number.sort()
print(number)


#  sorting list in decending order
number.sort(reverse=True)
print(number)


# Sorting string in a list - asscending order 
#  in length se check krta hai

fruits=["Apple","banana","grapes","Orange"]
fruits.sort()    # default by char asscending order
print(fruits)


#  sorting with a key

# asscendind order
fruits.sort(key=len)   # sort based on len
print(fruits)


# decendind order  - reverse = true - add
fruits.sort(key=len,reverse=True)   # sort based on len
print(fruits)





# 10 - pop with index value 
#  remove the value  index no se used pop 
#  not used index no  last value remove

number=[10,20,30,40]
popped = number.pop(2)
print(popped)     # output  - pop 2nd idex value 30 
print(number)


#  pop with defualt
#  used pop() not used index  last value remove 

last= number.pop()
print(last)    # output - pop last value by defult 40 
print(number)   # all value dikhta nhi hai repeat print varible




# 11 -  Copying list 
#  one varible copy by secand varble same value

fruit=["apple","banana","cherry"]
copy_fruit= fruit.copy()   # shallow copy
print(copy_fruit)

#  copy list - Modifying the copy does not affect 

# copy_fruit.append("Manog")
print(copy_fruit)    # add value
print(fruit)



#  Join List

list1=[1,2,3]
list2=['a','b','c']

#  using + operator

list3=list1 + list2
print(list3)

# 1-  using append method
for x in list1:
    list2.append(x)
    print(list2)   


#2-  Using extend method
list1.extend(list2)
print(list1) 



#  List Comprehensions

# synatax:
# list_name=[expression for item in iterable if condition]           
#  expression, for clasue , if condition

#  creat a list of  squares

square=[x**2 for x in range(1,6)]
print(square)


#  filter even number

even_list=[x for x in range(1,10) if x%2==0]
print(even_list)


#  increment number

number=[x+1 for x in range(1,10)]
print(number)


#  decement number

number=[x-1 for x in range(0,10)]
print(number)


#  apply function to each element of a list

my_list=['apple','mango','cherry']


#  nhi hog kyu ki list jo string hai aur list me nhi hai uppercase()
print(my_list.upper())    # this is wrong way


#  list compreshion
uppercase_list=[lst.upper() for lst in my_list ]
print(uppercase_list)


#  flatten a nested list using lis compreshion

nested_list=[[1,2],[3,4],[5,6]]

#  first , [1,2] -> 1,2
#  secand , [ 3,4] -> 3,4
#  thid , [ 5,6] -> 5,6



def  flatten_list(lst) :
     return [ item for sublist in lst for item in sublist]

final_list = flatten_list(nested_list)
print(final_list)


