#======================================================
#Python Functions
#======================================================
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function
def my_function():
    print("Assalamualaikum!")

#Calling a Function
my_function()

#Parameters
def mf(name):
    print("He is "+name)
mf("Abdul Karim")
mf("Abdul Rahim")
mf("Abdul Halim")

#Default Parameter Value
def mf(name = "Abdullah"):
    print("He is "+name)
mf("Abdul Karim")
mf()

#Passing a List as a Parameter
def mf(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry","litchi"]
mf(fruits)

#Return Values
def myr(x):
    return x*5
print(myr(10))
print(myr(20))
print(myr(30))

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
def mf(child3, child2, child1):
    print("The youngest child is "+child3)
mf(child2 = "Nusaybah", child1 = "Abdullah", child3 = "Mahera")

#Arbitrary Arguments
#If you do not know how many arguments that will be passed into your
#function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments,
#and can access the items accordingly:
def mf(*kids):
    print("The youngest child is "+kids[2])
mf("Nusaybah", "Abdullah", "Mahera")

#The pass Statement
#function definitions cannot be empty, but if you for some reason
#have a function definition with no content, put in the pass
#statement to avoid getting an error.
def myfunction():
  pass

#Recursion
'''
Python also accepts function recursion, which means
a defined function can call itself.

Recursion is a common mathematical and programming concept.
It means that a function calls itself. This has the benefit
of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it
can be quite easy to slip into writing a function which never
terminates, or one that uses excess amounts of memory or processor
power. However, when written correctly recursion can be a very
efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have
defined to call itself ("recurse"). We use the k variable as
the data, which decrements (-1) every time we recurse. The
recursion ends when the condition is not greater than 0
(i.e. when it is 0).

To a new developer it can take some time to work out how exactly
this works, best way to find out is by testing and modifying it.
'''
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)

'''
r 6 t5
    r 5 t4
        r 4 t3
            r 3 t2
                r 2 t1
                    r 1 t0
                        r = 0
                    r 1 t0=0
                r 2 t1=1
            r 3 t2=3
        r 4 t3=6
    r 5 t4=10
r 6 t5=15

r = 21
'''






