# 1)Python Program to Remove Punctuations From a String
def punc(str1):
    rem='''!()-[]{};:'"\,<>./?@#$%^&*_~'''     
    for i in str1:
        if(i in rem):
            str1=str1.replace(i,"")            
    
    print("New string is: ",str1)

n=input("Enter a string: ")
print("\n\nOriginal string is: ",n)
punc(n)

# 2)Python Program to Check Whether a String is Palindrome or Not
def palin(str1):
    return(str1 == str1[::-1])

n=input("Enter a string: ")
if(palin(n)):
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")



# 3)Python Program to Multiply Two Matrices using Nested List Comprehension
X = [[10,20,30],
    [40,50,60],
    [70,80,90]]
  
Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]

res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
res = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for i in res:
    print(i)


# 4)Python Program to Multiply Two Matrices using Nested Loop
X = [[10,20,30],
    [40,50,60],
    [70,80,90]]
  
Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]

res=[[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range (len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            res[i][j]+= X[i][k] * Y[k][j]
            
for i in res:
    print(i)


# 5)Python Program to Transpose a Matrix using Nested List Comprehension
X = [[10,20,30],
    [40,50,60],
    [70,80,90]]

res = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for i in res:
    print(i)