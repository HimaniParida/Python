# Splilting numpy arrays 
import numpy as np 
arr = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr,2)
print(new_arr)



import numpy as np 
arr = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr,4)
print(new_arr)



import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)






