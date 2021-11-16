import os
import sys
import getopt

options = ["srn:"]
options_long = ["shuffle", "reverse", "name"]

shuffle_flag = False
reverse_flag = False
name_flag = False
new_name = ""

def main():
    # parse arguments
    args, vals = getopt.getopt(sys.argv[1:], options, options_long)

    for arg, val in args:
        if arg in ("s", "--shuffle"):
            shuffle_flag = True
        elif arg in ("r", "--reverse"):
            reverse_flag = True
        elif arg in ("n", "--name"):
            name_flag = True
            new_name = val
    print("Shuffle:", shuffle_flag, "Reverse:", reverse_flag, "Name:", name_flag, "Newname:",new_name)

if __name__ == "__main__":
    main()