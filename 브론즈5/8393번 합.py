# 입력한 숫자까지의 합 구하기  : https://www.acmicpc.net/problem/8393

n = int(input())
total = 0

for i in range(1,n+1):
    total += i

print(total)