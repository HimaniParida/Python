import os

f = open('./Tutorial14/sample.txt')
g = open('./Tutorial14/sample.txt')
data1 = f.read()
data2 = g.read(7) # reads first 7 characters from the file
print(data1)
print(data2)
f.close()
g.close()


