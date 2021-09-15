import sys

n = int(sys.stdin.readline())

if 0 < n <= 100 and n%2 == 1:
    arr = [[" "]*n for _ in range(n)]
    c = 'A'
    half = n//2

    for i in range(half+1):
        for j in range(i*2+1):
            arr[half-i+j][half-i] = c
            if c == 'Z':
                c = 'A'
            else:
                c = chr(ord(c)+1)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
else:
    print("INPUT ERROR")


