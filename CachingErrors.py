try:
    value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
# handling errors - specific type (except is too broad)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
