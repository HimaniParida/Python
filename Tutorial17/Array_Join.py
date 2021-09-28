##### 1-D Arrays #####

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)


##### 2-D Arrays ####
import numpy as np
arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr2 = np.array([[11,12,13,14,15], [16,17,18,19,20]])
arr = np.concatenate((arr1,arr2), axis = 1)
print(arr)

#Joing arrays using stack functions 
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis = 1)
print(arr)


#Stacking along rows
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1,arr2))
print(arr)

#Stacking along columns
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1,arr2))
print(arr)


#Stacking along height
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print(arr)