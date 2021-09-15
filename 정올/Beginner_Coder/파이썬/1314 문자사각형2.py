import sys

n = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]
c = 'A'

for i in range(n):
    if i%2 == 0:
        for j in range(n):
            arr[j][i] = c
            if c == 'Z':
                c = 'A'
            else:
                c = chr(ord(c) + 1)
    else:
        for j in range(n):
            arr[n-j-1][i] = c
            if c == 'Z':
                c = 'A'
            else:
                c = chr(ord(c) + 1)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()