# 7) Write a Python Program to check if a number is prime or not
num = int(input("Enter a number: "))
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  


# 8) Python program to display all the prime numbers within an interval
lower = 0
upper = 20

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#  9) Python program to find the factorial of a number.
num = int(input("Enter a number: "))
factorial  = 1 
if num < 0 :
    print("Sorry, factorial doesn't exist for this number!!")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
           factorial = factorial*i
print("The factorial of",num,"is",factorial)

# 10) Python program to display the multipication table.
num = int(input("Enter a number: "))
print("Multiplication Table of : ")  
for i in range(1,11):    
   print(num,'x',i,'=',num*i)  


# 11) Python program to print the fibonacci series
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# 12) Python program to check the armstrong number 
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  