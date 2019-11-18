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

