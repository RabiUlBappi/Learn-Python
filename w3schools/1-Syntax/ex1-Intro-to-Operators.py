"""
This is comment
A multi line comment
Got it?
"""

if 5 > 2:
    print("Five is greater than two!")
        #print("OK")
    
x=5
x="Are you OK?"

print(x)
#print(y)

x,y,z='Are','you','OK?'
print(x)
print(y)
print(z)

print('Are you '+z)
print(x+y+z)


x='awsome'

def myfunc():
    x='fantastic'
    print('Python is '+x)


def myfunc1():
    global xx
    xx='OK'
myfunc1()
print(xx)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x=4
y=6
print(x)
print(y)
'''x,y^=y,x
print(x)
print(y)'''

#======================================================
#Python Strings
#======================================================

a = "Hello, World!"
print(a[1])
print(a[2:8])
print(a[-8:-2])
print(len(a))

a = " Hello, World! "
print(a.strip())
print(a.strip().lower())
print(a.strip().upper())
print(a.strip().replace("e","a").upper())
print(a.strip().split(","))

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
y = "a-in" in txt
z = "ain" not in txt
print(x)
print(y)
print(z)

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# String Format
age = 36
#txt = "My name is John, I am " + age #wrong statement
#print(txt)
txt = "My name is John, I am {}"
print(txt.format(age))

q=3
i=567
p=49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(q,i,p))

myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(q,i,p))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#======================================================
#Python Booleans
#======================================================

print(10 > 9)
print(10 == 9)
print(10 < 9)

a=2
b=4
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
print(bool("Hello"))
print(bool(15))    

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool('abc'))
print(bool(123))
print(bool(['ab','cd','ef']))

print(bool(False))
print(bool(True))

print(bool(None))
print(bool(''))
print(bool(""))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 1; #return 0;

myobj = myclass();
print(bool(myobj))

x = 200
print(isinstance(x, int))


#======================================================
#Python Operators
#======================================================

#Python Assignment Operators
#Assignment operators are used to assign values to variables
x=7
y=x
print(y)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%=3
print(x)
x=9
x//=3
print(x)
x=9
x**=2
print(x)
x=9
x&=3
print(x)
x=9
x|=3
print(x)
x=9
x^=3
print(x)
x=9
x>>=3
print(x)
x=9
x<<=3
print(x)



#Python Comparison Operators
#Comparison operators are used to compare two values:
print(bool(2 == 5))
print(bool(2 != 5))
print(bool(2 > 5))
print(bool(2 < 5))
print(bool(2 >= 5))
print(bool(2 <= 5))


#Python Logical Operators
#Logical operators are used to combine conditional statements
print(bool(2 < 5 and 8 < 7))
print(bool(2 < 5 or 8 < 7))
print(bool(not(2 < 5 and 8 < 7)))


#Python Identity Operators
#Identity operators are used to compare the objects,
#not if they are equal, but if they are actually the
#same object, with the same memory location:
x= 9
y = 2
print(bool(x is y))
print(bool(x is not y))


#Python Membership Operators
#Membership operators are used to test if a sequence is presented in an object
x = "I am Abdullah"
y = "bd"
print(bool(y in x))
print(bool(y not in x))


#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers
x = 6
y = 5
print(x & y) #4AND Sets each bit to 1 if both bits are 1
print(x | y) #7OR  Sets each bit to 1 if one of two bits is 1
print(x ^ y) #3XOR Sets each bit to 1 if only one of two bits is 1
print(~ x) #NOT Inverts all the bits
print(x << 1) #Zero-fill-left-shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(x >> 1) #Signed-right-shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off





