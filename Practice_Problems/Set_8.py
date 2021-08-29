# 1)Python Program Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def return_indices(li,target):
    store = dict()      
    for i in range(len(li)):
        sec = target - li[i]
        if sec not in store:
            store[li[i]]=i
        else:
            return [store[sec],i] 
        
list1= [7,9,11,14,21]
target=21
print("The indices are ",return_indices(list1,target))


# 2)Python Program Given a string, find the length of the longest substring without repeating characters.
def length(s):
    if(len(s)==0):
        return 0
    d={}
    max_len=0
    start=0
    
    for i in range(len(s)):
        if(s[i] in d and start<=d[s[i]]):
            start=d[s[i]]+1
        else:
            max_len=max(max_len,i-start+1)
                                           
        d[s[i]]=i                      
    return max_len

s=input("Enter a string(lowercase): ")
print("Length of longest substring is:",length(s))



# 3)ython Program to Count the Number of Each Vowel Using a list and a dictionary comprehension
vowels = 'aeiou'

string = input("Enter a string: ")
string = string.lower()

res = {}.fromkeys(vowels,0)        
                                   
for char in string:
    if char in res:
        res[char] += 1

print(res)
string = input("Enter a string: ")
string =string.lower()
res = {ans:sum([1 for char in string if char == ans]) for ans in 'aeiou'}

print(res)




##########################################################
# 4)Python Program to Illustrate Different Set Operations
s=set()

# adding one element in a set
s.add(1)
print(s)

# adding multiple elements in a set
s.update([1,2,3,4,8,9])       
print(s)

# to remove an element we use discard() or remove() 
s.discard(3)
print(s)

# pop() can also be used to remove elements but we cant determine which element will be removed
s.pop()
print(s)

# clear() removes all the element from a set
s.clear()
print(s)

# Set operations (Union) 
a={11,12,34,56}
b={5,6,7,8,9,10}
print(a | b)

# Set operations (Intersection)
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
print(a & b)

# Set operations (Set difference)
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
print(a - b)                    
print(b - a)  

# Set operations (Symmetric difference)
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
print(a ^ b)  
##################################################################


# 5)Python Program to Sort Words in Alphabet
def sort(s1):
    lis2=s1.split()              
    lis2.sort()
    for i in lis2:
        print(i)

n=input("Enter a sentence: ")
print("\nThe words in alphabetical order is as follows: ")
sort(n)