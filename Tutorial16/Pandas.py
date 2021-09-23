#Pandas-Pandas is a Python library used for working with data sets.It has functions for analyzing, cleaning, exploring, and manipulating data


import pandas
dict = {
  'phones' : ["Vivo", "Realme", "Redmi"],
  'price'  : [12000, 14000, 8000]
}

my_var = pandas.DataFrame(dict)

print(my_var)


