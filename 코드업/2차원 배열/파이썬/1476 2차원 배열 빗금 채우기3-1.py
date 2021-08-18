n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
num = 1

# 3 4 일때
# 00 -> i = 0, 합은 0, 1번
# 10 01 -> i = 1, 합은 1, 2번
# 20 11 20 -> i = 2, 합은 2, 3번
# 21 12 30 -> i = 3, 합은 3, 3번
# 22 13 -> i = 4, 합은 4, 2번
# 23 -> i = 5, 합은 5, 1번

for i in range(0, n+m-1):
    for j in range(0, m):  # 이렇게 해놔야 (1,0)부터 확인
        for k in range(0, n):
            if j+k == i:
                a[k][j] = num
                num += 1

for i in range(0, n):
    for j in range(0, m):
        print(a[i][j], end=' ')
    print()
