# 2588번 곱셈 : https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())

result = a*b
while True:
    print((b%10)*a)
    b //= 10
    if b == 0:
        break

print(result)
