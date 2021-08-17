n = int(input())

a = list(map(int, input().split()))

for i in range(0, len(a)):
    print(a.pop(), end=' ')