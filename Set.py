#   Set in python


#  Creat Set in python
#  There are two primary way to creat a set in python


# 1. Using Curly Braces {}

my_set={1,2,3,4,5}
print(my_set)



# 2. Using the set()  Constructor
list=[1,23,44,55]
print(type(list))   # list type
new_set=set(list)       # convert to set
print(new_set)



#  Note - An empty set conot be creat using{} as it creates dictinory. use set() instead

empty_set=set()
print(empty_set)    # output - set()



#  Set Opeations

# 1. Adding Element - use the add() method to add a simgle element to a set

fruits={"Apple","Banana"," cherry"," grapes","Orange"}
fruits.add("blackberry")   # add
print(fruits)


# 2. Rem{oveing() element - using the remove() or discard() method  to remove element
#   . remove() - raise an error if the element is not found
#    . discard() -  does not raise an error if the element is missing


furits={'apple','banana','cherry','blackberry'}

#  using remove()
#  set me not present element but remove kr rhe hai to error aaye ga

furits.remove('banana')
print(furits)


furits.discard('orange')    # if element is not present show error
print(furits)

#  using discard()
#  set me not present element but remove kr rhe hai to  error nhi aaye ga

furits.discard('orange')    #   if element is not present but not error
print(furits)


furits.discard('blackberry')    # remove
print(furits)



#  Set Methods

#  1. Union - combine element form two set , removing duplicate
#  repeat element not exist 

set_a={1,2,3,5}
set_b={2,4,6,5}

union_set =set_a.union(set_b)    # union 
print(union_set)

#  union alternative - used (|)

union_set=set_a| set_b
print(union_set)    # same used union 



#  2. intersection - lnclude only element present in both sets
#  same - same value in exist

set1={1,2,3,4}
set2={2,5,3,1}

inter_set = set1.intersection(set2)
print(inter_set)


#  intersection alternative

inter_set1=set1 & set2
print(inter_set1)    # same  used (&)


#  3. Difference - element present in first set only
#  but not in secand set

set1={1,2,3,4}
set2={3,4,5}

diff_set= set1.difference(set2)
print(diff_set)


#  difference alternative
diff_set1=set1- set2
print(diff_set1)


#  Symmertic Difference - element in either set but 
# not in both  (same-same value nhi leta two set)

set1={1,2,3,4}
set2={3,4,5,6}

sdiff_set=set1.symmetric_difference(set2)
print(sdiff_set)


#  Symmertric _ difference alternative

sdiff_set1=set1 ^ set2
print(sdiff_set1)      # same 



#  Set  Iteration 
#  you can use a for loop to get though each element in a first

#  using for loop - print each number from a set

number={1,2,3,4,5,6}

for set in number:
    print(set)


#  using while loop - first convert set to a list then use  while loop
# becouse sets do not support undex


#  not support



#  set comprehensions
#  set comprehension allow concise and readable creation of set Similar to
#  list comprehension but for set

#  syntax - 
#  new_set={expression for item in if condition}


Square={x**2 for x in range(1,6)}
print(Square)      # square 


even={x for x in range(1,8) if x%2==0}
print(even)       # even number


odd={x for x in range(1,8) if x % 2!=0}
print(odd)                 # odd number