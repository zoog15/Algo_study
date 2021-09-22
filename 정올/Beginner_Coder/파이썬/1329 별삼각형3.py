import sys

n = int(sys.stdin.readline())
half = n//2

if 0 < n <= 100 and n % 2 == 1:
    for i in range(half+1):
        for j in range(i):
            print(" ",end='')
        for k in range(i*2+1):
            print("*",end='')
        print()
    for i in range(half):
        for j in range(half-i-1):
            print(" ",end='')
        for k in range((half-i)*2-1):
            print("*",end='')
        print()
else:
    print("INPUT ERROR!")