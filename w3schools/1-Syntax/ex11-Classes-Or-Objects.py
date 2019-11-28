#=================================================
#Python Classes and Objects
#=================================================
#Python Classes/Objects
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class
#To create a class, use the keyword class:
class MyClass:
    x = 5

#Create Object
o1 = MyClass()
print(o1.x)

#The __init__() Function
'''
The examples above are classes and objects in their simplest form,
and are not really useful in real life applications.

To understand the meaning of classes we have to understand the
built-in __init__() function.

All classes have a function called __init__(), which is always
executed when the class is being initiated.

Use the __init__() function to assign values to object
properties, or other operations that are necessary to do
when the object is being created:
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Note: The __init__() function is called automatically every time
#the class is being used to create a new object.
o1 = Person("John", 36)
print(o1.name)
print(o1.age)

#Object Methods
#Objects can also contain methods. Methods in objects are
#functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def myfunc(self):
        print("Hello my name is "+self.name)

#Note: The self parameter is a reference to the current instance of 
#the class, and is used to access variables that belong to the class.
o1 = Person("John", 36)
o1.myfunc()

#The self Parameter
#The self parameter is a reference to the current instance of the
#class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class:

class Person:
    def __init__(notself, name, age):
        notself.name = name
        notself.age = age
        
    def mf(fnotself):
        print("My name is " + fnotself.name)
    
o1 = Person("John", 36)
o1.mf()

#Modify Object Properties
o1.age = 40

#Delete Object Properties
del o1.age

#Delete Objects
del o1
#o1.mf() #shows an error

#The pass Statement
#class definitions cannot be empty
class Person:
  pass

