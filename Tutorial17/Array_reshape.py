#Reshaping the array means changing the dimension of the array 

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10, 11,12])
newarr = arr.reshape(4,3)
print(newarr)


#Reshape from 1-D TO 3-D
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)


#checking its a copy or view
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)


#Unknown dimensions
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)


#Flattening the arrays
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)