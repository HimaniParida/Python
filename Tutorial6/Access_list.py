#Access items
my_list = ["apple", "banana", "cherry"]
print(my_list[2])

#negative_indexing
my_list = ["mango", "potato", "tomato","capsicum", "bitterguard"]
print(my_list[-2])

#rangeofindexes
my_list = ["apple", "banana", "cherry", "kiwi", "watermelon", "litchi", "apple","dates"]
print(my_list[2:5])

my_list = ["apple", "banana", "cherry", "kiwi", "watermelon", "litchi", "apple","dates"]
print(my_list[:4])

my_list = ["apple", "banana", "cherry", "kiwi", "watermelon", "litchi", "apple","dates"]
print(my_list[5:])

#rangeof negative indexes
my_list = ["apple", "banana", "cherry", "kiwi", "watermelon", "litchi", "apple","dates"]
print(my_list[-4 : -2])


#check if item exist
my_list = ["apple", "banana", "cherry", "kiwi", "watermelon", "litchi", "apple","dates"]
if "apple" in my_list:
    print("Yes , 'apple' is in this list")
