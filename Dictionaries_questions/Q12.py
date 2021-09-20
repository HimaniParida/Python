# 12.Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x':50, 'y':587, 'z': 156}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])