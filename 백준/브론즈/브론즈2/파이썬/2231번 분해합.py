# 분해합 : https://www.acmicpc.net/problem/2231

n = int(input())
answer = 0

for i in range(1, n):
    first = i
    sum_n = i
    while i != 0:
        sum_n += i%10
        i //= 10
    # print(sum_n)
    if sum_n == n:
        answer = first
        break

print(answer)
