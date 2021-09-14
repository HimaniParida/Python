# 1.Write a Python program to remove an item from a tuple
my_tuples = "h", "i", "m", "a", "n", "i", "p", "a", "r", "i", "d", "a"
print(my_tuples)
my_tuples = my_tuples[:2] + my_tuples[3:]
print(my_tuples)
listx = list(my_tuples) 
listx.remove("i") 
my_tuples = tuple(listx)
print(my_tuples)


# 2.Write a Python program to slice a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)
_slice = tuplex[5:]
print(_slice)
_slice = tuplex[:]
print(_slice)
_slice = tuplex[-8:-4]
print(_slice)
tuplex = tuple("HELLO WORLD")
print(tuplex)
_slice = tuplex[2:9:2]
print(_slice)
_slice = tuplex[::4]
print(_slice)
_slice = tuplex[9:2:-4]
print(_slice)


# 3. Write a Python program to find the index of an item of a tuple
tuplex = tuple("index tuple")
print(tuplex)
#get index of the first item whose value is passed as parameter
index = tuplex.index("p")
print(index)
#define the index from which you want to search
index = tuplex.index("p", 5)
print(index)
#define the segment of the tuple to be searched
index = tuplex.index("e", 3,6)
print(index)
 #if item not exists in the tuple return ValueError Exception
 #index = tuplex.index("y")


# 4.Write a Python program to find the length of a tuple.
tuplex = tuple("himaniparida")
print(tuplex)
print(len(tuplex))

# 5. Write a Python program to reverse a tuple
x = ("w3resource")
y = reversed(x)
print(tuple(y))
x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))


