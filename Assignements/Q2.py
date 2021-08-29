def avg_sales(sum,n):
    return(sum/n)
print("Let us calculate the average sales of the month\n")
sum_sales = count = 0
while(count<4):
    x = float(input("Enter the number sales in week {}: ".format(count+1)))
    sum_sales += x
    count += 1
average = avg_sales(sum_sales, count)
print("The average sales of this month is : ",average)
print("\n")