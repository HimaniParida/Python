def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

a=int(input("Enter a number to find its table: "))
table(a)