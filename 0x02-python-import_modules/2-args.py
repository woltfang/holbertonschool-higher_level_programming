#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} argument".format(len(sys.argv) - 1))
    for i in range (1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
