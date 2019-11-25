#======================================================
#Python Set
#======================================================
#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.
#Note: Sets are unordered, so you cannot be sure in
# which order the items will appear.

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Items
#You cannot access items in a set by referring to an index,
#since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask
#if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#Check if "banana" is present in the set:
print("banana" in thisset)

#Change Items
#Once a set is created, you cannot change its items,but you can add new items.

#Add Items
#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add more than one item to a set use the update() method.
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
# thisset.update({"orange", "mango", "grapes"})
print(thisset)

#Get the Length of a Set
print(len(thisset))

#Remove Item
#===========
#To remove an item in a set, use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
#Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("apple")
print(thisset)

#You can also use the pop(), method to remove an item,
#but this method will remove the last item. Remember that sets
#are unordered, so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

#Join Two Sets
#Note: Both union() and update() methods will exclude any duplicate items.
#There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates

#The union() method returns a new set with all items from both sets:
ts1 = {"apple", "banana", "cherry"}
ts2 = {"b", "c", "d"}
ts3 = ts1.union(ts2)
print(ts3)

#The update() method inserts the items in set2 into set1:
ts1 = {"apple", "banana", "cherry"}
ts2 = {"b", "c", "d"}
ts1.update(ts2)
print(ts1)

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Set Methods
#Python has a set of built-in methods that you can use on sets.
#==============================================================

#add()   Adds an element to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#clear() Removes all the elements from the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#copy()  Returns a copy of the set
thisset1 = {"apple", "banana", "cherry"}
thisset = thisset1.copy()
print(thisset)

#difference()    Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(x)
print(z)

#difference_update() Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#discard()   Remove the specified item
x = {"apple", "banana", "cherry"}
x.discard("apple")
print(x)

#intersection()  Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(x)
print(z)

#intersection_update()   Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#isdisjoint()    Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"google", "microsoft"}
print(x.isdisjoint(y))
print(x.isdisjoint(z))

#issubset()  Returns whether another set contains this set or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"google", "microsoft"}
print(x.issubset(y))
print(z.issubset(y))
print(y.issubset(z))

#issuperset()    Returns whether this set contains another set or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"google", "microsoft"}
print(x.issuperset(y))
print(z.issuperset(y))
print(y.issuperset(z))

#pop()   Removes an element from the set
z = {"google", "microsoft"}
print(z.pop())

#remove()    Removes the specified element
z = {"google", "microsoft"}
z.remove("google")
print(z)

#symmetric_difference()  Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x)

#symmetric_difference_update()   inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#union() Return a set containing the union of sets
ts1 = {"apple", "banana", "cherry"}
ts2 = {"b", "c", "d"}
ts3 = ts1.union(ts2)
print(ts3)

#update()    Update the set with the union of this set and others
ts1 = {"apple", "banana", "cherry"}
ts2 = {"b", "c", "d"}
ts1.update(ts2)
print(ts1)

