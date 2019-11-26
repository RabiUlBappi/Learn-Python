#======================================================
#Python Dictionary
#======================================================
#A dictionary is a collection which is unordered,
#changeable and indexed. In Python dictionaries are
#written with curly brackets, and they have keys and values.


#Create and print a dictionary:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
print(thisdict)


#Accessing Items
#by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)
#by get() method
x= thisdict.get("model")
print(x)


#Change Values
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
thisdict["year"] = 2019
print(thisdict)


#Loop Through a Dictionary
#looping returns the value of the keys of the dictionary
for x in thisdict:
    print(x)
#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
#values() function to return values of a dictionary
for x in thisdict.values():
    print(x)
#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)


#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  

#Dictionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(thisdict))


#Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#Removing Items
#pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem() method removes the last inserted item
#(in versions before 3.7, a random item is removed instead)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["year"]
print(thisdict)

#del keyword can also delete the dictionary completely
del thisdict
#print(thisdict)

#clear() keyword empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Copy a Dictionary
#use the built-in Dictionary method copy()
#in dict2 = dict1, dict2 will only be a reference to dict1
#changes made in dict1 will automatically also be made in dict2
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = thisdict2.copy()
print(thisdict)

#with the dict() method
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = dict(thisdict2)
print(thisdict)


#Nested Dictionaries
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
print(myfamily)
  
#Or, if you want to nest three dictionaries that already exists as dictionaries:
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
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

#The dict() Constructor
#It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford",model="Mustang",year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)



#Dictionary Methods

#clear() Removes all the elements from the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#copy()  Returns a copy of the dictionary
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = thisdict2.copy()
print(thisdict)

#fromkeys()  Returns a dictionary with the specified keys and values
x = ("key1","key2","key3")
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get()   Returns the value of the specified key
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.get("brand")
print(x)

#items() Returns a list containing a tuple for each key value pair
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.items()
for y in x:
    print(y)
for x, y in thisdict2.items():
    print(x, y)

#c()  Returns a list containing the dictionary's keys
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.keys()
print(x)
for y in x:
    print(y)
    
#pop()   Removes the element with the specified key
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.pop("brand")
print(x)
print(thisdict2)

#popitem()   Removes the last inserted key-value pair
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.popitem()
print(x)
print(thisdict2)

#setdefault()    Returns the value of the specified key.
#If the key does not exist: insert the key, with the specified value
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict2.setdefault("color","Red")
y = thisdict2.setdefault("model","Bronco")
print(x)
print(y)
print(thisdict2)

#update()    Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color":"White"})
print(car)

#values()    Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in car.values():
    print(x)










