#Accessing array elements
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[3])

#Accessing 2-D arrays
import numpy as np
arr = np.array([[1,2,3], [4,5,6]])
print(arr[0,1])


import numpy as np
arr = np.array([[1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]])
print(arr[1,5])

#Accessing 3-D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr[0,1,0])


#Negative indexing
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-1])