# 8. Write a Python program to multiply all the items in a dictionary. 
my_dict = {'data1':10,'data2':154,'data3':47}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print(result)
