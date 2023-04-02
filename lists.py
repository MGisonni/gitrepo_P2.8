### python script to create lists and plot them
import sys

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


# if function_number is 1, we plot the function f(x) = x
# otherwise, we give an error message
if function_number == 1:
    # we create two lists xval and yval
    xval = []
    yval = []

    # we populate xval with values from -5.0 to 5.0 (inclusive) with a step of 0.1
    for i in range(-50, 51):
        xval.append(i/10.0)

    # we populate yval with the values of the function f(x) = x
    for x in xval:
        yval.append(x)

elif function_number != 1:
    print("ERROR: Only function number 1 is implemented")
    sys.exit(1)