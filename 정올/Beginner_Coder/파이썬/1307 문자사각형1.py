import sys

n = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]
c = 'A'

for i in range(n):
    for j in range(n):
        arr[n-j-1][n-i-1] = c
        if c == 'Z':
            c = 'A'
        else:
            c = chr(ord(c) + 1)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()