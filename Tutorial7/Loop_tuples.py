#Loop through a tuple
my_tuple = ("apple", "banana", "cherry")
for x in my_tuple:
  print(x)


#Loop through the index numbers
my_tuple = ("apple", "banana", "cherry")
for i in range(len(my_tuple)):
  print(my_tuple[i])

#Using a while loop
my_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(my_tuple):
  print(my_tuple[i])
  i = i + 1