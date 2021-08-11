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
