n = int(input())

arr = [[" "]*(2*n-1) for _ in range(2*n-1)]

c = 'A'
x = 0
y = n-1
count = n
direct = [1,2,3,4]  # 왼쪽아래, 오른쪽아래, 오른쪽위, 왼쪽위

while True:
    for i in range(count-1):
        arr[x][y] = c
        x += 1
        y -= 1
        c = chr(ord(c)+1)
        if ord(c) == ord('Z')+1:
            c = 'A'
    for i in range(count-1):
        arr[x][y] = c
        x += 1
        y += 1
        c = chr(ord(c)+1)
        if ord(c) == ord('Z')+1:
            c = 'A'
    for i in range(count-1):
        arr[x][y] = c
        x -= 1
        y += 1
        c = chr(ord(c)+1)
        if ord(c) == ord('Z')+1:
            c = 'A'
    for i in range(count-1):
        arr[x][y] = c
        x -= 1
        y -= 1
        c = chr(ord(c)+1)
        if ord(c) == ord('Z')+1:
            c = 'A'
    x += 1
    count -= 1
    if count == 0:
        if ord(c) == ord('Z')+1:
            c = 'A'
        arr[x-1][y] = c
        break

for i in range(2*n-1):
    for j in range(2*n-1):
        print(arr[i][j], end=' ')
    print()
