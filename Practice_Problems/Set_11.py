# 1)Python Program to Make a Simple Calculator
def add(a,b):
      return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
def default():
  return "not found. Please try again!"

def cases(x,a,b):
    
    switch_case = {           
      1: add(a,b),
      2: sub(a,b), 
      3: mul(a,b),
      4: div(a,b)
    }
    
    res=switch_case.get(x,default())
    print("The answer is ",res)

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
choice=int(input("Enter a choice[Addition-1,Substraction-2,Multiplication-3,Division-4]: "))
cases(choice,n1,n2)


# 2)Python funcction to Find the Factors of a Number
def factors(n):
    mid=n // 2                                        
    for i in range(1,mid+1): 
        if(n % i == 0):             
            print(i,end=" ")                             
    print(n)                                          
    

a=int(input("Enter a number to find its factors: "))
print("The factors are :")
factors(a)


# 3)Python Program to Compute LCM Using GCD
def lcm(a, b):
    if a > b:
        smaller = a                      
    else:
        smaller = b
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            res = i 
    lcm=(a*b)/res                                  
    return lcm

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print("The L.C.M is", lcm(n1, n2))


# 4)write a Python function to Find LCM and returb the value
def lcm(a,b):
    if(a>b):
        max=a
    else:
        max=b
    while(True):
        if(max % a == 0 and max % b == 0):
            return max
        max+=1

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
print("The L.C.M is", lcm(n1, n2))