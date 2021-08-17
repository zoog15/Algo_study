n = int(input())  # n까지의 숫자카드
a = [0 for _ in range(n)]

for i in range(n-1):
    num = int(input())
    a[num-1] = 1

for i in range(len(a)):
    if a[i] == 0:
        print(i+1)