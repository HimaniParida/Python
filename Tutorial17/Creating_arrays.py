# creating a numpy ndarray Object
import numpy as np
array = np.array([1,2,3,4,5,6,7,8])
print(array)
print(type(array))

#creating a numpy using tuple
import numpy as np
array = np.array((1,2,3))
print(array)


#######################################################################33#DIMESIONS IN ARRAYS###########################################################################33

#0-D arrays
import numpy as np
arr = np.array(42)
print(arr)

#1-D arrays
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)

#2-D arrays
import numpy as np
arr = np.array([[1,2,3],[6,7,8]])
print(arr)

#3-D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


#CHECKING THE DIMENSIONS
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)