#======================================================
#Python Tuples
#======================================================
#A tuple is a collection which is ordered and unchangeable.
#In Python tuples are written with round brackets.
#Allows duplicate members.

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access Tuple Items
print(thistuple[1])

#Negative Indexing
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Range of Negative Indexes
#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Change Tuple Values
#Once a tuple is created, you cannot change its values.
#Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list,
#change the list, and convert the list back into a tuple.

x = ("apple","banana","cherry")
print(x)
y = list(x)
y.insert(1, "orange")
x = tuple(y)
print(x)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for x in thistuple:
    print(x)

#Check if Item Exists
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "kiwi" in thistuple:
    print("Yes, 'kiwi' is is the fruits tuple.")

#Tuple Length
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(len(thistuple))

#Add Items
#Once a tuple is created, you cannot add items to it.
#Tuples are unchangeable.
thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" # This will raise an error
print(thistuple)

#Create Tuple With One Item
#To create a tuple with only one item, you have to
#add a comma after the item, unless Python will not
#recognize the variableas a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Remove Items
#Tuples are unchangeable, so you cannot remove items from it,
#but you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
del thistuple
#print(thistupel) #this will rais an error

#Join Two Tuples
#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(type(thistuple))

#Tuple Methods
#Python has two built-in methods that you can use on tuples.

#count() Returns the number of times a specified value occurs in a tuple
thistuple = ("apple", "banana", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple.count("banana"))

#index() Searches the tuple for a specified value and returns the position of where it was found
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple.index("banana"))
print(thistuple.index("kiwi"))
















