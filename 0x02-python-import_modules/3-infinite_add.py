#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            s += int(sys.argv[i])
    print(s)