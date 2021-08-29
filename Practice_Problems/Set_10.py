# 1)Python Program to Transpose a Matrix using Nested Loop
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

res = [[0,0,0],
      [0,0,0],
      [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
         res[j][i] = X[i][j]

for i in res:
    print(i)


# 2)Python Program to Add Two Matrices using Nested List Comprehension
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
  
Y = [[11,12,13],
    [14,15,16],
    [17,18,19]]

res = [[0,0,0],
       [0,0,0],
       [0,0,0]]
 
for i in range(len(X)):
    for j in range(len(X[0])):
        res[i][j] = X[i][j] + Y[i][j]
        
for i in res:
    print(i)


# 3)Python Program to Find Factorial of Number Using Recursion
def fact(n):
    if (n>=1):
        return n*fact(n-1)
    else:
        return 1;

a=int(input("Enter a number: "))
print("The factorial is :",fact(a))


# 4)Python Program to Find Sum of Natural Numbers Using Recursion
def recur_sum(n):
    if (n != 0):
        return n + recur_sum(n - 1);
    else:
        return n;

a=int(input("Enter a number: "))
print("The sum is :",recur_sum(a))

# 5)Python Program to Display Fibonacci Sequence Using Recursion
def fibo(n):
       if n <= 1:
            return n

       return(fibo(n-1) + fibo(n-2))


c=int(input("Enter number of terms: "))
print("Fibonacci sequence:")
for i in range(c):
    print(fibo(i),end=" ")