#======================================================
#Python Lambda
#======================================================
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments,
#but can only have one expression.

#Syntax
x = lambda a : a + 10
print(x(10))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
 
def mf(n):
    return lambda a : a * n
nf = mf(3)
print(nf(3))
 