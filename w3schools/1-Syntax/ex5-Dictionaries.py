#======================================================
#Python Dictionaries
#======================================================
#A dictionary is a collection which is unordered, changeable and
#indexed. In Python dictionaries are written with curly brackets,
#and they have keys and values.

#Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Accessing Items
#You can access the items of a dictionary by referring to its key name,
#inside square brackets:
x = thisdict["model"]

#There is also a method called get() that will give you the same result:
x = thisdict.get("model")

#Change Values
#You can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys
#of the dictionary, but there are methods to return the values as well.
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
#Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Dictionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
#Print the number of items in the dictionary:
print(len(thisdict))

#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() keyword empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in method dict().
#Make a copy of a dictionary with the dict() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#A dictionary can also contain many dictionaries, this is called nested dictionaries.
#Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or, if you want to nest three dictionaries that already exists as dictionaries:
#Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#The dict() Constructor
#It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.

#clear() Removes all the elements from the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#copy()  Returns a copy of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
td = thisdict.copy()
print(td)

#fromkeys()  Returns a dictionary with the specified keys and values
k = ["k1","k2","k3"]
v = 0
i = dict.fromkeys(k, v)
print(i)

#get()   Returns the value of the specified key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get("brand"))

#items() Returns a list containing a tuple for each key value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
    print(x, y)

#keys()  Returns a list containing the dictionary's keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
    
#pop()   Removes the element with the specified key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

#popitem()   Removes the last inserted key-value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.setdefault("color", "White")
thisdict.setdefault("year", 2019)
print(thisdict)

#update()    Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

#values()    Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
