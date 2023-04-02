### python script to create lists and plot them
import sys
import matplotlib.pyplot as plt
import math 


# create a dictionary with numbers and name of handled functions
functions = {1: "f(x) = x", 2: "f(x) = x^2", 3: "f(x) = x^3", 4: "f(x) = sin(x)", 5: "f(x) = cos(x)", 6: "f(x) = tan(x)"}

# the script takes a number as input from command line. 
# We reprint it here to check it is working fine.
# if no number is given, we print an error message.
if len(sys.argv) == 1:
    print("ERROR: No number given, expected one number")
    print("The following functions are implemented:")
    for key in functions:
        print("  "+str(key)+": "+functions[key])
    sys.exit(1)
elif len(sys.argv) == 2:
    print("Number", sys.argv[1], "was passed")
    function_number = int(sys.argv[1])
else:
    print("ERROR: Too many arguments, expected one number")
    sys.exit(1)

# we plot the handled functions and print an error message if the function is not handled
if function_number in functions.keys():
    # we create two lists xval and yval
    xval = []
    yval = []

    # we populate xval with values from -3.0 to 3.0 (inclusive) with a step of 0.1
    for i in range(-30, 31):
        xval.append(i/10.0)

    # we populate yval with the values of the function f(x) = sin/cos/tan(x) and plot it
    for x in xval:
        if function_number == 1:
            yval.append(x)
        elif function_number == 2:
            yval.append(x**2)
        elif function_number == 3:
            yval.append(x**3)
        elif function_number == 4:
            yval.append(math.sin(x))
        elif function_number == 5:
            yval.append(math.cos(x))
        elif function_number == 6:
            yval.append(math.tan(x))

    # we plot the values of xval and yval
    print("Plotting function number "+str(function_number)+", i.e. "+functions[function_number])
    plt.plot(xval, yval)
    plt.title("Plot of "+functions[function_number])
    plt.show()

else:
    print("ERROR: function number "+str(function_number)+" is not implemented")
    print("The following functions are implemented:")
    for key in functions:
        print("  "+str(key)+": "+functions[key])    
    sys.exit(1)