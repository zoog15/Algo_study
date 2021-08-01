# 1292번 쉽게 푸는 문제 : https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
m = []
cnt = 0; num = 1; sum = 0; idx = 1

for i in range(0, b):
    if num == cnt:
        num += 1
        cnt = 0
    m.append(num)
    cnt += 1

for i in m:
    if idx < a:
        idx += 1
        continue
    sum += i

print(sum)
