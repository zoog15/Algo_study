n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    b.append(a[i])

b.sort()

for i in range(n):
    print(b.index(a[i]),end = ' ')