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
else:
    print("ERROR: Too many arguments, expected one number")
    sys.exit(1)

