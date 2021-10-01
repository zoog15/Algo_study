n, m = map(int, input().split())
chess = [[0]*m for _ in range(n)]
# print(*chess,sep='\n')


def check(i,j):
    minB = 0  # B로 시작하는 비교 최소값
    minW = 0  # w로 시작하는 비교 최소값
    start_i = i
    start_j = j
    for i in range(8):
        for j in range(8):
            if chess[start_i+i][start_j+j] != check1[i][j]:
                minB += 1
            if chess[start_i+i][start_j+j] != check2[i][j]:
                minW += 1

    return min(minB, minW)


check1 = [ # B로 시작하는 체스판
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]
check2 = [  # W로 시작하는 체스판
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]

for i in range(n):  # 체스판 입력
    chess[i] = list(input())

# print(*chess,sep='\n')

min_change = n*m  # 전부다 바꿔야할때가 나올수있는 최대값
for i in range(n-7):
    for j in range(m-7):
        if check(i,j) < min_change:
            min_change = check(i,j)

print(min_change)






