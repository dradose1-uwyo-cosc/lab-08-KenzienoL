# Mackenzie Bailey
# UWYO COSC 1010
# 7 Nov 2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# Austin


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

        # needs negitive
        # check int or float
            # int has no decimal
            # float has one decimal
        # convert
        # return if not

def num_convert(num):           # Thanks Austin

    isNeg = False       # negitive set

    if '-' in num:      # checks for negitive
        isNeg = True
        num = num.replace('-', '')

    if '.' in num:      # checks if float
        num_list = num.split('.')
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():      # checks if valid float
            if isNeg:
                return -1 * float(num)      # neg convert
            else:
                return float(num)       # pos convert
    
    elif num.isdigit():     # checks if int
        if isNeg:
            return -1 * int(num)        # neg convert
        else:
            return int(num)     # pos convert
    
    else:
        return False
    

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

m = 0           # initallized before
b = 0
upper = 0
lower = 0

def slope_intercept(m, b, lower, upper):
    m = num_convert(m)
    if m == False:      # checks valid input          # Austin pointed out that booleans are integers. He told me not to worry about the 'conditions' 
        print('Invalid slope')                        # but this is why 0 is not a valid input
        return False                                  # And why below it says 'float'
    
    b = num_convert(b)
    if b == False:
        print('Invalid intercept')
        return False

    lower = num_convert(lower)
    upper = num_convert(upper)

    if upper is float or lower is float:    # checks numerical valid input 
        print('Invalid bounds')
        return False
    if upper < lower:       # checks if upper is greater than lower
        print('Upper bound must be greater than lower bound')
        return False

    outputs = []

    for i in range(lower, upper + 1):
        # print(i, "   ", m, "   ", b)
        y = m * i + b
        # print(y)
        outputs.append(y)
    return(outputs)

while True:
    if input("Exit to quit: ").upper() == 'EXIT':
        break
    else:
        m = input("Enter slope: ")
        b = input("Enter y-intercept: ")
        lower = input("Enter lower bound: ")
        upper = input("Enter upper bound: ")

        si = slope_intercept(m, b, lower, upper)

        if si == False:
            continue
        else:
            print(si)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

a = 0
b = 0
c = 0

def sqrt(value):
    y = (value)**(1/2)
    return(y)

def quad_formula(a, b ,c ):
    a = num_convert(a)
    b = num_convert(b)
    c = num_convert(c)

    if a == False:      # checks valid input
        print('Invalid a')
        return False
    if b == False:      # checks valid input
        print('Invalid b')
        return False
    if c == False:      # checks valid input
        print('Invalid c')
        return False

    value_1 = (b + sqrt(b**2 - (4 * a * c))) / (2 * a)
    value_1 = str(value_1)
    if 'j' in value_1:
        value_1 = 'null'
    value_2 = (b - sqrt(b**2 - (4 * a * c))) / (2 * a)
    value_2 = str(value_2)
    if 'j' in value_2:
        value_2 = 'null'
    values = [value_1, value_2]
    return(values)

while True:
    if input("Exit to quit: ").upper() == 'EXIT':
        break
    else:
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")

        qf = quad_formula(a, b, c)

        if qf == False:
            continue
        else:
            print(qf)