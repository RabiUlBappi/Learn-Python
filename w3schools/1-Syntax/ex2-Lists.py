#======================================================
#Python Lists
#======================================================
#List is a collection which is ordered and changeable.
#Allows duplicate members and written with square brackets.

#Create a list
thislist = ["apple","banana","cherry"]
print(thislist)

#Access items
print("\n"+thislist[1])

#Negative Indexing
#Negative indexing means beginning from the end,
#-1 refers to the last item,
#-2 refers to the second last item etc.
print("\n"+thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\n")
print(thislist[2:5])

#Range of Negative Indexes
print("\n")
print(thislist[-6:-3])

#Change Item Value
thislist = ["apple","banana","cherry"]
thislist[1] = "kela"
print("\n")
print(thislist)

#Loop Through a List
thislist = ["apple","banana","cherry"]
print("\n")
for x in thislist:
    print(x)

#Check if Item Exists
thislist = ["apple","banana","cherry"]
print("\n")
if "banana" in thislist:
    print("Yes, banana is in the fruits list.")

#List Length
thislist = ["apple","banana","cherry"]
print("\n")
print(len(thislist))



#Add items
#=========

#by append() to the last
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print("\n")
print(thislist)

#by insert() to specified index
thislist = ["apple","banana","cherry"]
thislist.insert(2, "orange")
print("\n")
print(thislist)



#Remove Item
#===========

#remove() method removes the specified item
thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print("\n")
print(thislist)

#pop() method removes the specified index,
#(or the last item if index is not specified)
thislist = ["apple","banana","cherry"]
print("\n")
thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)
print(thislist.pop(0)) #prints the poped/removed item

#del keyword removes the specified index
thislist = ["apple","banana","cherry"]
del thislist[1]
print("\n")
print(thislist)

#del keyword can also delete the list completely:
thislist = ["apple","banana","cherry"]
print("\n")
print(thislist)
del thislist
#print(thislist)

#clear() method empties the list
thislist = ["apple","banana","cherry"]
print("\n")
print(thislist)
thislist.clear()
print(thislist)

#Copy a List
#You cannot copy a list simply by typing list2 = list1,
#because: list2 will only be a reference to list1, and
#changes made in list1 will automatically also be made in list2.

#make reference to the list
thislist = ["apple","banana","cherry"]
print("\n")
print(thislist)
nlist = thislist
print(nlist)
thislist.insert(1, "orange")
print(thislist)
print(nlist)

#copy of a list with the copy() method
thislist = ["apple","banana","cherry"]
print("\n")
print(thislist)
nlist = thislist.copy()
print(nlist)
thislist.insert(1, "orange")
print(thislist)
print(nlist)

#copy of a list with the built-in method list() 
thislist = ["apple","banana","cherry"]
print("\n")
print(thislist)
nlist = list(thislist)
print(nlist)
thislist.insert(1, "orange")
print(thislist)
print(nlist)

#Join Two Lists
#join two lists using the + operator
thislist1 = ["apple","banana","cherry"]
thislist2 = ["orange","nuts","grapes"]
thislist = thislist1 + thislist2
print("\n")
print(thislist)

#join two lists are by appending all the items from
#list2 into list1,one by one
thislist1 = ["apple","banana","cherry"]
thislist2 = ["orange","nuts","grapes"]
print("\n")
for x in thislist2:
    thislist1.append(x)
print(thislist)

#use the extend() method
thislist1 = ["apple","banana","cherry"]
thislist2 = ["orange","nuts","grapes"]
print("\n")
thislist1.extend(thislist2)
print(thislist1)

#The list() Constructor
#It is also possible to use the list() constructor to make a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print("\n")
print(thislist)


#Different List Methods
#Python has a set of built-in methods that you can use on lists.
#===============================================================
#append()    Adds an element at the end of the list
print("\n")
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#clear() Removes all the elements from the list
thislist.clear()
print(thislist)

#copy()  Returns a copy of the list
thislist1 = ["apple","banana","cherry"]
thislist = thislist1.copy()
print(thislist)

#count() Returns the number of elements with the specified value
thislist = ["apple","banana","cherry","banana","banana"]
bananaNO = thislist.count("banana")
print(bananaNO)

#extend()    Add the elements of a list (or any iterable), to the end of the current list
thislist1 = ["apple","banana","cherry"]
thislist2 = ["orange","papya"]
thislist1.extend(thislist2)
print(thislist1)

#index() Returns the index of the first element with the specified value
thislist = ["apple","banana","cherry","banana","banana"]
bananaIndex = thislist.index("banana")
print(bananaIndex)
cherryIndex = thislist.index("cherry")
print(cherryIndex)

#insert()    Adds an element at the specified position
thislist = ["apple","banana","cherry"]
thislist.insert(0, "orange")
print(thislist)

#pop()   Removes the element at the specified position
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)

#remove()    Removes the item with the specified value
thislist = ["apple","banana","cherry"]
thislist.remove("apple")
print(thislist)

#reverse()   Reverses the order of the list
thislist = ["apple","banana","cherry"]
thislist.reverse()
print(thislist)

#sort()  Sorts the list
thislist = ["banana","cherry","apple"]
thislist.sort()
print(thislist)

