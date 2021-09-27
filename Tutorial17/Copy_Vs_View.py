###############################################################3#DIFFERENCE BETWEEN COPY AND VIEW########################################################33
#he main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy
#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.


#copy
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


#view
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)


#Making changes in the view
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

#Checking if array owns it's data
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()  #copy returns none
y = arr.view()  #view returns the original array
print(x.base)
print(y.base)




