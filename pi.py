def printPi (dec=10):
    pi=3.0;
    flag=1;
    n = 2.0;
    for i in range(10000000):
        if flag:
            pi+= 4/(n * (n+1) * (n+2))
            n+=2
            flag=0
        else:
            pi-= 4/(n * (n+1) * (n+2))
            n+=2
            flag=1

    print("{0:.{1}f}".format(pi, dec))

if __name__ == "__main__":
    import sys
    printPi(int(sys.argv[1]))
