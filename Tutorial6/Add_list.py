#Append() - This function is used to add items in the list using Append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend() - This function is udes to add the items from one list to another
my_list = ["apple", "mango", "banana"]
this_list = ["potato", "tomato", "capsicum"]
my_list.extend(this_list)
print(my_list)

#Add any iterable 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
