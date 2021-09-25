# 6.Reverse pyramid of numebers
rows = 6 
for row in range(1,rows):
    for columns in range(row,0,-1):
        print(columns, end=' ')
    print(" ")