# 1546번 평균 : https://www.acmicpc.net/problem/1546

n = int(input())

score = list(map(int, input().split()))
sum_n = 0
max_n = max(score)

for i in range(n):
    if score[i] < max_n:
        score[i] = score[i]/max_n * 100
    elif score[i] == max_n:
        score[i] = 100
    sum_n += score[i]

print(sum_n/n)