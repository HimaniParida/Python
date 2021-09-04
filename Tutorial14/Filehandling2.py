import os

f = open('./Tutorial14/sample2.txt')
# read first line
data = f.readline() 
print(data)

# Read second line and so on...
data = f.readline() 
print(data)
f.close()