# 1)write a program to multiply two Matrix 
def matrix_multiplication(M, N):
    R = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]
 
    for i in range(0, 4):
        for j in range(0, 4):
            print(R[i][j], end =" ")
        print("\n", end ="")
M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
N = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]

matrix_multiplication(M, N)


# 2)write a program to calculate exponents of an input
def calc_exponent(base,exponent):
    return base ** exponent

b=int(input("Enter the base number: "))
e=int(input("Enter the exponent number: "))
print("Result :",calc_exponent(b,e))

# 3)Python Program Given a list slice it into a 3 equal chunks and revert each list
def slice_revert(list1):
    x = [list1[i:i + 3] for i in range(0, len(list1), 3)] 
    reversed_list = [elem[::-1] for elem in x ]            
    print(reversed_list)

slice_revert([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


# 4)Python Program to Rotate an array of n elements to the right by k steps.
def rotate(li,k):
    n=len(li)
    list1=[]
    list1[:]=li[k:n] + li[0:k]
    return list1

li=[11, 12, 13, 14, 15, 16, 17]
val=int(input("Enter the value of k: "))
print("Original list is :",li)
print("New list after rotation is :",end=' ')
print(rotate(li,val))
     


# 5)Python Program Given a sorted integer array without duplicates, return the summary of its ranges.
def summary(li):
    start=0
    res=[]
    
    for i in range(len(li)):
        if (i+1 < len(li) and li[i]+1 == li[i+1]):         
                continue                                    
                
        if start == i:
            res.append(str(li[start]))                      
        else:
            res.append(str(li[start]) + "->" + str(li[i]))
                                                            
        start=i+1                                           
    return res

list1=[0,1,2,3,6,7,9,11]
print("Summary is :", summary(list1))