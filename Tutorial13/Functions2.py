#Parameters /Arguments - The both terms i.e. :  parameter and argument can be used for the same thing information that are passed into a function.

def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Himani", "Parida")




#######################################################
#Arbitary argumnets - If we do not know how many arguments that will be passed into our created function, we can add a * before the parameter name in the function definition.
def my_function(*kids):
      print("The youngest child is " + kids[1])

my_function("Himani", "Subhasmita", "Shakti")



########################################################
#Keyword arguments - We can also send arguments with the key = value syntax. 
def my_function(child3, child2, child1):
      print("The youngest child is " + child2)

my_function(child1 = "Himani", child2 = "Subhasmita", child3 = "Shakti")



######################################################
#Arbitary keyword arguments , **kwargs- If we do not know how many keyword arguments that will be passed into our function, add two asterisk:
#  ** before the parameter name in the function definition
def my_function(**kid):
      print("Her last name is " + kid["lname"])

my_function(fname = "Himani", lname = "Parida")

#################################################
#Default Parameter value - If we call the function without argument, it uses the default value:
def my_function(country = "Australia"):
      print("I am from " + country)

my_function("Russia")
my_function("India")
my_function()
my_function("Tokyo")


##########################################
#Recursion - Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
def printPattern(targetNumber) :
  if (targetNumber <= 0) :
    print(targetNumber)
    return
 
  print(targetNumber)
  printPattern(targetNumber - 5)
  print(targetNumber)
 

n = 10
printPattern(n)


###############################################
#Scope - 
def fun():
    print(s)
s=input("Enter a string : ")
fun()



##################################################
#List Comprehension
l1=[12,3,45,52,60,7,5,2]
l2=[]
for i in l1:
    if(i>3):
        l2.append(i)
print(l1)   
print(l2)


#Add  numbers in the list 
def add_list(l):
    s=0
    for i in l:
        s=s+i
    return s    
l= list(map(int,input("Enter the numbers of the list : ").split(" ")))
print("The numbers in the list are {}".format(l))
print("The sum of the numbers in the list is {}".format(add_list(l)))

