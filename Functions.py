# Functions

def say_hi(name, age):
    print("Hello " + name + " You are " + str(age))

# Giving it parameters - Calling statements
say_hi("Peter",50)
say_hi("Steve",30)

# Return Statements
def cube(num):
    return num*num*num
# return breaks out of the function
# cannot print anything else after that

result = cube(4)
print(result)






