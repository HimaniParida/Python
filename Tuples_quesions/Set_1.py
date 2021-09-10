# 1.Write a Python program to create a tuple with different data types.
tuples = ("tuple", False, 3.2, 1)
print(tuples)


# 2.Write a Python program to create a tuple with numbers and print one item
tuplex = 5, 10, 15, 20, 25
print(tuplex)
tuplex = 5,
print(tuplex)


# 3.Write a Python program to unpack a tuple in several variables
#tuples = 4, 8, 3 
#print(tuples)
#n1, n2, n3 = tuples
#print(n1 + n2 + n3) 
#n1, n2, n3, n4= tuples

# 4.Write a Python program to add an item in a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
listx = list(tuplex) 
listx.append(30)
tuplex = tuple(listx)
print(tuplex)


# 5.Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)


# 6.Write a Python program to get the 4th element and 4th element from last of a tuple
my_tuple = ("h","i","m","a","n","i","p","a","r","i","d","a")
print(my_tuple)
item = my_tuple[3]
print(item)
item1 = my_tuple[-4]
print(item1)

# 7.Write a Python program to create the colon of a tuple.
from copy import deepcopy
tuplex = ("HELLO", 5, [], True) 
print(tuplex)
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)

# 8.Write a Python program to find the repeated items of a tuple
my_tuple = 1,2,4,5,5,3,7,8,
print(my_tuple)
count = my_tuple.count(5)
print(count)

# 9.Write a Python program to check whether an element exists within a tuple. 
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)

# 10.Write a Python program to convert a list to a tuple. 
listx = [5, 10, 7, 4, 15, 3]
print(listx)
tuplex = tuple(listx)
print(tuplex)
