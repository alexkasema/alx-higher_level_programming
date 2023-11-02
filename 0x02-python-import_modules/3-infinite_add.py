#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    av = sys.argv
    ac = len(sys.argv)
    sum = 0

    if ac == 1:
        print("0")
        sys.exit()
    else:
        for i in range(1, ac):
            sum += int(av[i])
    print(sum)
