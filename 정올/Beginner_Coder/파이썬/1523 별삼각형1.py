import sys

n, m = map(int, sys.stdin.readline().split())

if 0 < n <= 100 and 1 <= m <= 3:
    if m == 1:
        for i in range(n):
            for j in range(i+1):
                print("*",end='')
            print()
    elif m == 2:
        for i in range(n):
            for j in range(n-i):
                print("*",end='')
            print()
    elif m == 3:
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end='')
            for k in range(2*i+1):
                print("*",end='')
            print()

else:
    print("INPUT ERROR!")