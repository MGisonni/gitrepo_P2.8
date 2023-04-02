### python script to create lists and plot them
import sys
import matplotlib.pyplot as plt
import math 

# the script takes a number as input from command line. 
# We reprint it here to check it is working fine.
# if no number is given, we print an error message.
if len(sys.argv) == 1:
    print("ERROR: No number given, expected one number")
    sys.exit(1)
elif len(sys.argv) == 2:
    print("Number", sys.argv[1], "was passed")
    function_number = int(sys.argv[1])
else:
    print("ERROR: Too many arguments, expected one number")
    sys.exit(1)


handled_functions = [2, 3, 4]
# if function_number belongs to {2,3,4} we plot the function f(x) = sin/cos/tan(x) respectively
# otherwise, we give an error message

# we create a dictionary with the function names
function_names = {2: "sin", 3: "cos", 4: "tan"}

if function_number in handled_functions:
    # we create two lists xval and yval
    xval = []
    yval = []

    # we populate xval with values from -5.0 to 5.0 (inclusive) with a step of 0.1
    for i in range(-50, 51):
        xval.append(i/10.0)

    # we populate yval with the values of the function f(x) = sin/cos/tan(x) and plot it
    for x in xval:
        if function_number == 2:
            yval.append(math.sin(x))
        elif function_number == 3:
            yval.append(math.cos(x))
        elif function_number == 4:
            yval.append(math.tan(x))

    print("Plotting function number "+str(function_number)+", i.e "+function_names[function_number]+"(x)")
    plt.plot(xval, yval)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Plot of "+function_names[function_number]+"(x)")
    plt.show()

    # close the plot and exit
    plt.close()
    sys.exit(0)

    
else:
    print("ERROR: Function number "+str(function_number)+" is not implemented")
    print("Implemented functions are: "+str(handled_functions))
    sys.exit(1)