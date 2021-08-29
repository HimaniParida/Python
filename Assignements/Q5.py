def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    print(f"The fact of {n} is",res)

a=int(input("Enter a number to find its fact: "))
fact(a)