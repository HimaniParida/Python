# 1. Write a Python program to sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# 2. Write a Python program to multiply all the items in a list
def multiply_list(items):
    multiply = 1
    for x in items:
        multiply *= x
    return multiply
print(multiply_list([1,2,-8]))

# 3. Write a python program to get the largest number from the list.
def largest_number(items):
    max = items[ 0 ]
    for a in items:
        if a > max:
            max = a
    return max
print(largest_number([1, 2, -8, 0]))

# 4. Write a python program to get the smallest number from the list.
def min_num(items):
    min = items[0]
    for a in items:
        if a < min:
            min = a 
    return min
print(min_num([1, 2, -9, 8]))

# 5. Write a Python program to remove duplicates from a list
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

# 6. Write a Python program to check a list is empty or not
l = []
if not l:
  print("List is empty")
  

# 7.Write a Python program to clone or copy a list
list1 = [10, 52, 64, 27, 4]
list2 = list(list1)
print(list1)
print(list2)


# 8.Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "She turned her can't into can and dreams into plans"))


#9. Write a Python function that takes two lists and returns True if they have at least one common member
def com_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(com_data([1,2,3,4,5], [5,6,7,8,9]))
print(com_data([1,2,3,4,5], [6,7,8,9]))


# 10.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


