# Panda Series - A Pandas Series is like a column in a table.It is a one-dimensional array holding data of any type.

import pandas as pd
a = [1, 74, 12]
myvar = pd.Series(a)
print(myvar)


# Key/value objects as series

import pandas as pd
calories = {"day1": 425, "day2": 480, "day3": 350}
myvar = pd.Series(calories)
print(myvar)


# 