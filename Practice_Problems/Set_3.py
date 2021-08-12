# 13) find the sum of the cube of each digit in python 
num = int(input("Enter a number: "))
sum = 0
while(num > 0):
    sum = sum + (num % 10) * (num % 10) * (num % 10)
    num = num // 10
print("Sum of each cubes =" , sum)


# 14) python program to find an armstrong number in an interval
lower = 2
upper = 200
for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)

# 15) Python Program to Find the Sum of Natural Numbers
num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# 16) Python Program to Find Numbers Divisible by Another Number
my_list = [23, 43, 21 , 45, 69]
result = list(filter(lambda x: (x % 3== 0), my_list))
print("Numbers divisible by 3 are",result)


# 17) Python Program to Convert Decimal to Binary
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
if __name__ == '__main__':
    dec_val = 24
    DecimalToBinary(dec_val)


# 18) Python Program to Convert Decimal to Hexadecimal
def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while(j >= 0):
        print((hexaDeciNum[j]), end="")
        j = j - 1
n = 2545
decToHexa(n)
 