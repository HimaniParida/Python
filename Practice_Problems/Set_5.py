# 1) Join two sets

s1 = {"apple", "ball" , "cat"}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)


# 2)Sort the string list alphabetically
friends = ['Himani', 'Merry', 'Chandan', 'Pratyusha', 'Vicky', 'Tapaswini']
friends.sort()
print(friends)


# 3)Set the values in the new list to upper case

input = ['fun', 'Foo', 'BaR']
lst = [x.upper() for x in input]
print(lst)


# 4)Generate a list by list comprehension
squares = []
for i in range(10):
     squares.append(i * i)
squares

# 5)Access first and Last characters in a string
string="This is a string"
last_char=string[-1]     #last characters of string
first_char=string[0]     #first characters of string
print(first_char,last_char)
string="This is a sample string"

def last(string):
    string=string + " "       

    for i in range(len(string)):
        if(string[i]== ' '):
            print(string[i-1],end=" ")

def first(string):
    res= ""
    v = True
    for j in range(len(string)):
        if(string[j] == ' '):
            v = True
        elif(string[j] != ' ' and v == True):
            res+=string[j]+' ' 
            v=False
    
    return res

print(last(string))
print(first(string))

