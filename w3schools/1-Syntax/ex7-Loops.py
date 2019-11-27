#======================================================
#Python Loops
#======================================================

#The while Loop
#==================
i = 1
while i < 6:
  print(i)
  i += 1

# while 1: print("infinite\n")

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
#The else Statement
#With the else statement we can run a block of code once
#when the condition no longer is true:
i = 5
while i < 5:
    print(i)
    i+=1
else: print("i is no longer less than 5")



#Python For Loops
#==================
#A for loop is used for iterating over a sequence
#(that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages,
#and works more like an iterator method as found in other
#object-orientated programming languages.
#With the for loop we can execute a set of statements,
#once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)
  
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
#To loop through a set of code a specified number of times,
#we can use the range() function,
#The range() function returns a sequence of numbers,
#starting from 0 by default, and increments by 1 (by default),
#and ends at a specified number.
for x in range(6):
  print(x)

#The range() function defaults to 0 as a starting value
for x in range(22, 26):
  print(x)

#The range() function defaults to increment the sequence by 1,
#however it is possible to specify the increment value by adding a
#third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement
for x in [0, 1, 2]:
  pass









