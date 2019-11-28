#=================================================
#Python Inheritance
#=================================================
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class,
#also called derived class.

#Create a Parent Class
#Any class can be a parent class, so the syntax is the same
#as creating any other class:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

#Create a Child Class
#To create a class that inherits the functionality from another class,
#send the parent class as a parameter when creating the child class:
class Student(Person):
    pass
#Now the Student class has the same properties and
#methods as the Person class.

o2 = Student("John", "Smith")
o2.printname()

#Add the __init__() Function
#So far we have created a child class that inherits
#the properties and methods from its parent.
#We want to add the __init__() function to the child
#class (instead of the pass keyword).

class Student(Person):
    def __init__(self, fname, lname):
        pass #add properties etc.

#When you add the __init__() function, the child class will
#no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance
#of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function,
#add a call to the parent's __init__() function:
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
#Now we have successfully added the __init__() function,
#and kept the inheritance of the parent class, and we are
#ready to add functionality in the __init__() function.

#Or
        
#Use the super() Function
#Python also has a super() function that will make the child
#class inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#By using the super() function, you do not have to use the name
#of the parent element, it will automatically inherit the methods
#and properties from its parent.
        
#Add Properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

#In the example below, the year 2019 should be a variable,
#and passed into the Student class when creating student objects.
#To do so, add another parameter in the __init__() function:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Add Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#If you add a method in the child class with the same name
#as a function in the parent class, the inheritance of the
#parent method will be overridden.

o1 = Student("John", "Doe", 2019)
o1.welcome()



