# 11050번 이항계수1 : https://www.acmicpc.net/problem/11050
N, K = map(int, input().split())

answer = 1
for i in range(N, N-K,-1):
    answer *= i

for i in range(1, K+1):
    answer //= i

print(answer)


