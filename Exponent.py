# Exponent using For Loops

# Two pieces of information
def raise_to_power(base_num,pow_num):
    # Result is the store of the maths
    result = 1
    # Loop through the range of numbers from 1 to the power number of times
    for index in range(pow_num):
        # Multiplying result by base num
        result = result * base_num
    return result

print(raise_to_power(3,4))
