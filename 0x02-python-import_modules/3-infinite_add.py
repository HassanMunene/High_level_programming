#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    le = sys.argv
    sum = 0
    for i in range(1, len(le)):
        sum = sum + int(le[i])
    print("{}".format(sum))
