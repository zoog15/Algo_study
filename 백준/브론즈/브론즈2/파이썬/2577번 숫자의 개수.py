# 2577번 숫자의 개수 : https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

arr = [int(0) for _ in range(10)]  # 0으로 길이 10 배열 초기화

mul = int(a*b*c)  # a*b*c한값

while True:
    if mul == 0:
        break
    mod = mul % int(10)
    arr[mod] += 1
    mul //= 10;

for i in arr:
    print(i)