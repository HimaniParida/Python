#For loops - A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping through a string
fruits = ["apple", "banana", "cherry"]
for x in "banana":
      print(x)


#The break statement
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

#The continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range function - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
fruits = ["apple", "banana", "cherry"]
for x in range(6):
  print(x)



#Else in for loop
fruits = ["apple", "banana", "cherry"]
for x in range(6):
      print(x)
else:
  print("Finally finished!")


#Nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass statements
fruits = ["apple", "banana", "cherry"]
for x in [0, 1, 2]:
      pass

