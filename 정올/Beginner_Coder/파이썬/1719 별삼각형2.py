import sys

n, m = map(int, sys.stdin.readline().split())
half = n//2

if 0 < n <= 100 and n%2 == 1 and 1 <= m <= 4:
    if m == 1:
        for i in range(half+1):
            for j in range(i+1):
                print("*",end='')
            print()
        for i in range(half):
            for j in range(half-i):
                print("*",end='')
            print()
    if m == 2:
        for i in range(half+1):
            for j in range(half-i):
                print(" ",end='')
            for k in range(i+1):
                print("*",end='')
            print()
        for i in range(half):
            for j in range(i+1):
                print(" ",end='')
            for k in range(half-i):
                print("*",end='')
            print()
    if m == 3:
        for i in range(half+1):
            for j in range(i):
                print(" ",end='')
            for k in range((half-i)*2+1):
                print("*",end='')
            print()
        for i in range(half):
            for j in range(half-i-1):
                print(" ",end='')
            for k in range((i+1)*2+1):
                print("*",end='')
            print()
    if m == 4:
        for i in range(half+1):
            for j in range(i):
                print(" ",end='')
            for k in range(half+1-i):
                print("*",end='')
            print()
        for i in range(half):
            for j in range(half):
                print(" ",end='')
            for k in range(i+2):
                print("*",end='')
            print()
else:
    print("INPUT ERROR!")