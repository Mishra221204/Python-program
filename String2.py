#  String in python 
# Indexing , Slicing and Method

#  string  Indexing - Positive & Negative
#  space bhi count hota hai
#  positive index- first character 0 hota hai 
#  Negative index =  last charcter se start (-1 to any sting)

# Positive   
my_name="shubham"
# index- 0,1,2,3,4,5,6 first char
print(my_name[0])
print(my_name[1])
print(my_name[2])
print(my_name[3])
print(my_name[4])
print(my_name[5])
print(my_name[6])

# negative index
name="Madhav"
# index= -1,-2,-3,-4,-5,-6 last
print(name[-1])  # last chara
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6]) # first chara print

#  space count

value="hello World"
print(value[6])



#  Slicing  String
#  syntax- string[start : end: step]

#  star- start in string 
#  end - end in string 
#  step - defalt string in 1,2 line chhod kare

my_name="Shubham"
print(my_name[0])   # start

print(my_name[0 : 6])  # stat and end

print(my_name[0:6:1])  # start , end  and step

print(my_name[0:6:2])

print(my_name[3:6:1])

print(my_name[0:6:3])
print(my_name[:])   # all charac
print(my_name[::])   # all charc

print(my_name[-1:-6:-1])  # negative index string  
print(my_name[::-1])  # reverse the string

#  String method
world="hello ,world"


#  1. len()
print(len(world))

#  2. upper()
print(world.upper())

#  3. upper()
print(world.lower())

# 4. count ()
print(world.count("o"))   # count krta hai kitne time aaya hai
print(world.count("l"))


# 5. find()
#  position btata hai index number kitne per hai charc
print(world.find("o"))
print(world.find("h"))


# 6 . split ()
# chac ko split krta hai kisi sepred ke bich me
print(world.split(","))   #  chac ke bch me (,) used huaa hai to split (,) me hoga
print(world.split())   # blank joge to vo charc ke bich me spilt kre ga


# 7. Replace ()
#  syntac-  replace( old , new)
print(world.replace("world","Shubham"))


#  8 .Tittle()
#  Isse first charc capital krta hai
print(world.title()) 


# 9. strip ()
#  start and end  space ko catta hai
world2="  Hello Shubham  "
print(world2.strip())



# 10 . join()
world3=("My", "name" ,"is")
print("_ ".join(world3))