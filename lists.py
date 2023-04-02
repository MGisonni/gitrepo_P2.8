### python script to create lists and plot them
import sys
import matplotlib.pyplot as plt
import math 


# create a dictionary with numbers and name of handled functions
functions = {1: "f(x) = x", 2: "f(x) = exp(x)", 3: "f(x) = sqrt(|x|)"}

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


# if function_number is 1,2 or 3, we plot the corresponding function
# otherwise, we give an error message
if function_number in functions.keys():
    # we create two lists xval and yval
    xval = []
    yval = []

    # we populate xval with values from -5.0 to 5.0 (inclusive) with a step of 0.1
    for i in range(-50, 51):
        xval.append(i/10.0)

    # we populate yval with the values of the corresponding function
    if function_number == 1:
        for x in xval:
            yval.append(x)
    elif function_number == 2:
        for x in xval:
            yval.append(math.exp(x))
    elif function_number == 3:
        for x in xval:
            yval.append(math.sqrt(abs(x)))
    
    # we plot the function
    print("Plotting function numer "+str(function_number)+": "+functions[function_number])
    plt.plot(xval, yval)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Plot of "+functions[function_number])
    plt.show()



elif function_number != 1:
    print("ERROR: function number "+str(function_number)+" is not implemented")
    print("The following functions are implemented:")
    for key in functions:
        print("  "+str(key)+": "+functions[key])
    sys.exit(1)