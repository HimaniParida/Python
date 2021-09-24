# What is a dataframe - A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd 

dict = {
    'days' : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    'calories' : [469, 457, 442, 389, 320, 202]
}

table = pd.DataFrame(dict)

print(table)


#locating a row:
print(table.loc[4])


#naming the indexes 
import pandas as pd 

dict = {
    'days' : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    'calories' : [469, 457, 442, 389, 320, 202]
}

table = pd.DataFrame(dict, index = ["day1", "day2", "day3", "day4", "day5", "day6"])

print(table)



import pandas as pd

table = pd.read_csv('dict.csv')

print(table) 
