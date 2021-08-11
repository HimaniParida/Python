# 1)Python program to convert kilometers to miles
kilometers = float(input("enter the value in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print("%0.2f kilometers is equal to %0.2f miles" %(kilometers,miles))


# 2)Python program to convert celsius to fahrenheit
celsius = float(input('Enter temperature in Celsius: '))  
fahrenheit = (celsius * 1.8) + 32  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))  

# 3)Python Program to Check if a Number is Positive, Negative or 0
n = float(input("Enter a number: "))    #Using if...elif....else
if n > 0:
   print("Positive number")
elif n == 0:
   print("Zero")
else:
   print("Negative number")


n = float(input("Enter a number: "))    #Using nested if
if n >= 0:
   if n == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")


# 4)Python Program to Check if a Number is Odd or Even
n = float(input("Enter a number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 5)Python Program to Check Leap Year
year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  


# 6)Python Program to Find the Largest Among Three Numbers
a =  float(input("Enter the first numbers: "))
b = float(input("Enter the second number"))
c = float(input("Enter the third number"))
if (a > b) and (a > c):
    print("a is largest")
elif (b > a) and (b > c):
    print("b is largest")
else:
    print("c is largest")


