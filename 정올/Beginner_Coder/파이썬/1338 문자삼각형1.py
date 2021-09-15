import sys

h = int(sys.stdin.readline())
arr = [[" "]*h for _ in range(h)]
c = 'A'

for i in range(h):
    for j in range(h-i):
        arr[i+j][h-1-j] = c
        if c == 'Z':
            c = 'A'
        else:
            c = chr(ord(c)+1)

for i in range(h):
    for j in range(h):
        print(arr[i][j],end=' ')
    print()
