### python script to create lists and plot them
import sys
import matplotlib.pyplot as plt


# create a dictionary with numbers and name of handled functions
functions = {1: "f(x) = x"}

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


# if function_number is 1, we plot the function f(x) = x
# otherwise, we give an error message
if function_number == 1:
    # we create two lists xval and yval
    xval = []
    yval = []

    # we populate xval with values from -3.0 to 3.0 (inclusive) with a step of 0.1
    for i in range(-30, 31):
        xval.append(i/10.0)

    # we populate yval with the values of the function f(x) = x
    for x in xval:
        yval.append(x)

    # we plot the values of xval and yval
    print("Plotting function number "+str(function_number)+", i.e. f(x) = x")
    plt.plot(xval, yval)
    plt.show()
    plt.close()

elif function_number != 1:
    print("ERROR: function number "+str(function_number)+" is not implemented")
    print("The following functions are implemented:")
    for key in functions:
        print("  "+str(key)+": "+functions[key])
    sys.exit(1)