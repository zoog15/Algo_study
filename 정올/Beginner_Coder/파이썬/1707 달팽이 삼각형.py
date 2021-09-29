import sys

n = int(sys.stdin.readline())  # 사각형의 크기

square = [[0]*n for _ in range(n)]  # n x n 크기의 사각형 만들기 및 0 초기화
num = 1
move = n
x = 0; y = -1  # 첫 시작 좌표

while move > 0:
    for i in range(move):
        y += 1
        square[x][y] = num
        num += 1

    move -= 1
    for i in range(move):
        x += 1
        square[x][y] = num
        num += 1

    for i in range(move):
        y -= 1
        square[x][y] = num
        num += 1

    move -= 1
    for i in range(move):
        x -= 1
        square[x][y] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()