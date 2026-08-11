#    File Handling in python

#  syntax-
#  file_object=opean('filename', 'mode')

#  file modes
# . r = read (default mode) mode me kuch nhi dalo ge to (read lega)
# . w = Write
# . a = Append file last me
# . rb/wb = write in binary mode


#  Open ()  file

file=open('Example.txt', 'r')


#  read file    read(),readline() , readlines()

file = open('Example.txt', 'r')
content = file.read()    # read entire   data
print(content)
file.close()   # best practies


#   readline() 

file = open('Example.txt', 'r')
content = file.readline()    # read  first line 
print(content)
file.close()  



#   readlines() - read all line in  convert to (list formate) 

file = open('Example.txt', 'r')
content = file.readlines()    #  list entire data
print(content)
file.close()  



#   Write to a file
#  write()  - write in string
# writeline() - write in string and list

# file= open('example1.txt','w')   # write mode - over write krta hai
# file.write("Namaste, Kaise ho")
# file.close()


#  over write na kre iske liye used (Append())
#  append()- char to add last me  next line me


# file= open('example1.txt','a')   # append mode
# file.write("\n Acha hu")
# file.close()



#  close a file 
#  Method used

#  using  ( with statement)

with open('example1.txt','r') as file:
    content= file.read()
print(content)    



# --------------------------------------------------------------------------------------------------------------------------------------

#   Q1. Slove  write a file

#  write()
file=open('example2.txt','w')
file.write("Hello Shubham Mishra\n"
           "kaise ho Aap")
file.close()


#  read file  useing with statement close file

with open('example2.txt','r') as file:
    content=file.read()
print(content)


#  Add aur charac in file used (append())

with open('example2.txt','a') as file:
    file.write("\nI am fine")


# #  read used output value check

with open('example2.txt','r')  as file :

  content=file.read()
print(content)





#  Wb/rb - write/ read  in binary number
#  write() argument must be str, not bytes used (append)


#  Wb - write binary number - b'a=number'
file=open('example3.txt','wb')
file.write(b'd=11001')    # wb n=binary number



# rb- read binary number

with open('example3.txt','rb') as file :
     content=file.read()
print(content)



