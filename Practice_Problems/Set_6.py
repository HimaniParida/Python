# 1)Returns the number of times the specified element appears in the list
def count_elements(l1,key):
    c=0
    for i in l1:
        if (i == key):
            c+=1
    return c

l1=[8,6,8,10,20,10,3,8,2,8]
x=int(input("Enter the number to be counted: "))
print(f"{x} was present {count_elements(l1,x)} times in the list")


# 2)Python program to Sort the list in descending order
def sort_list(li):
    for i in range(1, len(li)):  
        value = li[i]  
        j = i - 1  
        while j >= 0 and value > list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
        list1[j + 1] = value   
    print("Descending order:",list1)
    
list1=[18, 0, -3 , 23, 34]
sort_list(list1)

# 3)Python program to Sort the list in ascending order
def sort_list(li):
    for i in range(1, len(li)):  
        value = li[i]  
        j = i - 1  
        while j >= 0 and value < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
        list1[j + 1] = value   
    print("Ascending order:",list1)
    
list1=[18, 0, -3 , 23, 34]
sort_list(list1)


# 4Python program to compute sum of digits in number)
def sum_of_digits(n):
    li=[]
    sum=0
    for i in n:
        sum=sum+ (int(i))
    print("Sum of digits is",sum)

a=input("Enter a number: ")
sum_of_digits(a)

#5)write a program to find and print the remainder of two number
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
if(n > m):
    print("Remainder:",n%m)
else:
    print("Remainder:",m%n)