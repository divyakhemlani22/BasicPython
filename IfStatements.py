# If Statements
# Help to make decisions and have other things and other data
# We deal with it everyday

is_Male = False
is_Tall = True

# Using AND / OR
if is_Male and is_Tall:
    print("You are a Tall Male")
elif is_Male and not(is_Tall):
    print("You are a Short Male")
elif not(is_Male) and is_Tall:
    print("You are a Tall Female")
else:
    print("You are a Short Female")

# returning largest number
def max_num(num1,num2, num3):
    # The result will either be true or false
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(3,40,5))

# Can compare all different data types - int, string, float etc

# Better Calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print (num1/num2)
elif op == "*":
    print (num1*num2)
else:
    print("Invalid Operator")

# Dictionary
# Store information and key value pairs
monthConversions = {
    1: "January",
    2: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
}

# Can specify default value if key is not found
print(monthConversions.get("Luv", "Not a Valid Key"))
print(monthConversions["Dec"])








