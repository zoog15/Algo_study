a, b = map(int, input().split())

arr = []

for i in range(a):
    arr.append([])
    for j in range(b):
        arr[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:  # 가로
            arr[x-1][y-1+j] = 1
        else:  # 세로
            arr[x-1+j][y-1] = 1

for i in range(a):
    for j in range(b):
        print(arr[i][j], end=' ')
    print()
