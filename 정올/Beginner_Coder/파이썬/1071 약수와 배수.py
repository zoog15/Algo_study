import sys

n = int(sys.stdin.readline())  # 입력받을 정수의 개수
arr = list(map(int, sys.stdin.readline().split()))  # 정수들 입력
m = int(sys.stdin.readline())

sum1 = 0  # 약수의 합
sum2 = 0  # 배수의 합

for i in arr:
    if m % i == 0:
        sum1 += i
    if i % m == 0:
        sum2 += i

print(sum1)
print(sum2)
