#======================================================
#Python Conditions and If statements
#======================================================

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#Indentation
#Python relies on indentation (whitespace at the beginning of a line)
#to define scope in the code. Other programming languages often use
#curly-brackets for this purpose.
a = 33
b = 200
#if b > a:
#print("b is greater than a") # you will get an error

#Elif
#The elif keyword is pythons way of saying
#"if the previous conditions were not true, then try this condition".
a = 33
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")

#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 34
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is less than b")
#You can also have an else without the elif:
a = 22
b = 33
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

#Short Hand If
if a < b: print("a is less than b")

#Short Hand If ... Else
print("a is big") if a > b else print("b is big")

#One line if else statement, with 3 conditions:
a = 33
b = 33
print("A") if a > b else print("=") if a == b else print("B")

#And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true.")

#Or
a = 200
b = 33
c = 50
if a > b or c > a:
    print("At least one of the conditions is True.")

#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
#if statements cannot be empty, but if you for some reason have
#an if statement with no content, put in the pass statement
#to avoidgetting an error.
a = 33
b = 200

if b > a:
  pass


    








