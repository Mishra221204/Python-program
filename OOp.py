#  OOPs in python
#  OOP - object oriented programing


#  Using list - creating student record 

student1=["shubham",10]   # Name, Grade
student2=["Shivam",12]

print(student1)
print(student1[0])

print(f" Name is {student1[0]} an Grand is {student1[1]}")
print(f" Name is {student2[0]} an Grand is {student2[1]}")



#  ------------------------------------------------------------------------------------------------------------------------------------------------

#  using OOps - creating student records

#  class - blueprint or template  - class name  me first letter capital
#  __init__ method- constructor,value initialize - fix    - Method creat used def __init__(self-parameter pass)
#  Self parameter - reference or connection  build btw
# # class and object - fix

class Student :    # student class
     
     def __init__(self,name,age,grade,father_name,section):   # method  first method __inite__ (aur any used any name)
          self.name=name   # attribute 
          self.age=age     # attribute 
          self.grade=grade  # attribute 
          self.father_name=father_name   
          self.section=section

     def student1(self):     # secand method not used __init__
          print(f"{self.name} is in class {self.grade}")

     def student2(self): 
          print(f"Student Name {self.name} in class {self.grade} and section {self.section}")

#  # Object - instance of class
#  #  class ki help se object creat ( varible aur class name)

Student_detail= Student("Shubham",20,12,"Manoj Kumar Mishra","A")
print(f"Student Name is {Student_detail.name} and Father name is  {Student_detail.father_name} Student grade {Student_detail.grade}")
          

Student_detail1= Student("Shivam",10,10,"Manoj Mishra","B")
print(f"Student Name is {Student_detail1.name} and Father name is {Student_detail1.father_name} Student grade {Student_detail1.grade}")


# #  acesss
Student_detail.student1()
Student_detail1.student2()


#  dictionary fome me convert
print(Student_detail.__dict__)


# #  Modify object property

Student_detail1.section = "C"   # modify  
print(Student_detail1.section)


#  Delete object  propert
print(Student_detail.__dict__)
del Student_detail.age
print(Student_detail.__dict__)



# #  Delete object
del Student_detail
print(Student_detail) # delet


#  Q ------------------------------------------------------------------------------------------------------------------------------------

#  varible ke sath  link

#  class - blueprint or template  - class name  me first letter capital

class Student :    # student class
     
     def __init__(self,name,age,grade,father_name,section,team):   # method  first method __inite__ (aur any used any name)
          self.name=name   # attribute 
          self.age=age     # attribute 
          self.grade=grade  # attribute 
          self.father_name=father_name   
          self.section=section
          self.team= team


     def student1(self):     # secand method not used __init__
          print(f"{self.name} is in class {self.grade}")

team1="A"     # link object ke sath 
team2="B" 

 # Object - instance of class
 #  class ki help se object creat ( varible aur class name)

Student_detail= Student("Shubham",20,12,"Manoj Kumar Mishra","A",team1)
print(f"Student Name is {Student_detail.name} and Father name is  {Student_detail.father_name} Student grade {Student_detail.grade} and team {team1}")
          

Student_detail1= Student("Shivam",10,10,"Manoj Mishra","B",team2)
print(f"Student Name is {Student_detail1.name} and Father name is {Student_detail1.father_name} Student grade {Student_detail1.grade} and team {team2}")

#  acesss value

print(Student_detail.team)
print(Student_detail1.team)

Student_detail.student1()   # call the student method
print(Student_detail)





#  Q-------------------------------------------------------------------------------------------------------
#  4 Features in OOps
#  1. Abstraction
#  2. Encapsulation
#  3. Inheritance
#  4. Polymorphism



#  1. Abstrction  :-  hiding unnecesary  details form users  through  Method , Class
# kisi value ko hidde kr skte hai user se help of Abstraction  ya method me class me 

class Student :    # student class
     
     def __init__(self,name,age,grade):  
          self.name=name   # attribute 
          self.age=age      
          self.grade=grade  
          
     def student1(self):      # method
          print(f"{self.name} is in class {self.
          grade+2}")  # hidden form user



#  # Object - instance of class

Student_detail= Student("Shubham",20, 12)
Student_detail1= Student("Shivam",15,  10)


print(Student_detail.names)


#2. Encapsulation 
# Restrict access to certain attributes or method to protect data and enforce controlled access
# aur direct access nhi kr skte hai Method se acces kr skte hai
#  private krne ke liye used  (double underscore limits)

class Student :    # student class
     
     def __init__(self,name,age,grade):  
          self.name=name   # attribute 
          self.age=age      
          self.__grade=grade   # double underscore limits
          
     # def student1(self):      # method
     #      print(f"{self.name} is in class {self.grade+2}")  

     # def get_grade(self):      # private access used Method 
     #      return self.__grade
  
 # Object - instance of class

Student_detail= Student("Shubham",20, 12)
Student_detail1= Student("Shivam",15,  10)


print(Student_detail.__grade)   # errors
print(Student_detail.grade)     # error

print(Student_detail.get_grade())  # acesss





# 3.   Inheritanc
#  allow one class (child) to reuse to prop and method another 
#  class(parent)    class and method inheritace

#   parent class-baap
class Student :    # student class
     def __init__(self,name,age,grade):  
          self.name=name   # attribute 
          self.age=age      
          self.grade=grade  
          
     def student1(self):      # method
          print(f"{self.name} is in class {self.
          grade+2}") 

 # Object - instance of class

Student_detail= Student("Shubham",20, 12)
Student_detail1= Student("Shivam",15,  10)


#  child class-beta
#  super() se hmm parent class ke value ko acess krte hai

class GraduateStudent(Student):   # GraduateStudent class inheritance proparties
     #  and method from student parent class
     def __init__(self, name, age, grade,steam):  # old parameters from parent class and
          #  new parameters  in child class
          super().__init__(name, age, grade)   # call parent class init
          self.stream=steam   # new attribute in child class

     def student_function(self):
      super().student1()    # method inherit from parent class
      print(f'stream is  {self.stream}')

#  Object 

Grad_student= GraduateStudent('Madhav',20,12,'science')
print(Grad_student.stream)

Grad_student.student_function()  # call           







#  4. Polymorphism
#  Allow  method in different class to have same name but different value
#  depending on object 



class Student :    # student class
     def __init__(self,name,age,grade):  
          self.name=name   # attribute 
          self.age=age      
          self.grade=grade  
          
     def student1(self):      # method
          print(f"{self.name} is in class {self.
          grade+2}") 


 # Object - instance of class

Student_detail= Student("Shubham",20, 12,'MATH')
Student_detail1= Student("Shivam",15,  10)



#   child class

class GraduateStudent(Student):  
     def __init__(self, name, age, grade,steam):  
          super().__init__(name, age, grade)   
          self.stream=steam   

     def student_function(self):   # method 
      print(f'{self.name}  in  year {self.age }   and grade is {self.grade} with Stream {self.stream}')


#  Object  - student class 
Student_detail= Student("Shubham",20, 12)

#  object - GraduateStudent class 
Grad_student= GraduateStudent('Madhav',20,12,'science')


Grad_student.student_function()  # differnt access

Student_detail.student_funtion()  # different acess value diferent