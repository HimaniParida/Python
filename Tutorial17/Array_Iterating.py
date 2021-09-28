#Array iterating means going through the element one by one 

import numpy as np
arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)

### 2-D Arrays###
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)


### 3-D Arrays###
import numpy as np
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for x in arr:
    print(x)

#Iteraring down to the scalars
import numpy as np
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for x in arr:
      for y in x:
        for z in y:
            print(z)


#Iterating arrays using nditer()
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

#Iterating arrays with different data types
import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


#Iterating array with different step size
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

#Enemurated iteration using ndenumerate()
import numpy as np
arr = np.array([1, 2, 3])   # 1-D arrays
for idx, x in np.ndenumerate(arr):
  print(idx, x)


import numpy as np
arr = np.array([[1,2,3], [4,5,6]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)