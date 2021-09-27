#checking the data type of an array

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

import numpy as np
arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)


#Creating array with a defined data type 
import numpy as np
arr = np.array([1,2,3,4,5] , dtype = 'S')
print(arr)
print(arr.dtype)

import numpy as np
arr = np.array([1,2,3,4,5], dtype = 'i4')
print(arr)
print(arr.dtype)


#Converting data type on existing arrays
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)


