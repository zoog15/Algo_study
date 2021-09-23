import sys

n = int(sys.stdin.readline())
arr = [[0] * i for i in range(1,n+1)]  # 삼각형 모양(계단) 배열 생성

num = 0
x = -1
y = -1

for i in range(n):
    for j in range(i,n):
        if i % 3 == 0:  # 아래쪽으로 갈때
            x += 1
            y += 1
        elif i % 3 == 1:  # 왼쪽으로 갈때
            y -= 1
        else:
            x -= 1  # 위로갈때
        arr[x][y] = num%10
        num += 1

for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end=' ')
    print()
