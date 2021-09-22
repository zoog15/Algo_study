import sys

n, m = map(int, sys.stdin.readline().split())

if 0 < n <= 100 and n % 2 == 1 and 1 <= m <= 3:
    if m == 1:
        num = 1
        arr = [[0]*i for i in range(1,n+1)]

        for i in range(n):
            for j in range(i+1):
                if i % 2 == 0:
                    arr[i][j] = num
                    num += 1
                else:
                    arr[i][len(arr[i])-j-1] = num
                    num += 1

        for i in range(n):
            for j in range(i+1):
                print(arr[i][j],end=' ')
            print()
    elif m == 2:
        num = 0
        for i in range(n):
            for j in range(i):
                print(" ",end=' ')
            for k in range((n-i)*2-1):
                print(num,end=' ')
            print()
            num += 1
    elif m == 3:
        half = n//2
        for i in range(half+1):
            num = 1
            for j in range(i+1):
                print(num,end=' ')
                num += 1
            print()
        for i in range(half):
            num = 1
            for j in range(half-i):
                print(num,end=' ')
                num += 1
            print()
else:
    print("INPUT ERROR!")