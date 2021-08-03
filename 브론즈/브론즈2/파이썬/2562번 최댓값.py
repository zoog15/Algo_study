# 2562번 최댓값 : https://www.acmicpc.net/problem/2562

max = -1
cnt = 1
max_cnt = 0

for i in range(0,9):
    n = int(input())
    if n > max:
        max = n
        max_cnt = cnt
    cnt += 1

print(max)
print(max_cnt)