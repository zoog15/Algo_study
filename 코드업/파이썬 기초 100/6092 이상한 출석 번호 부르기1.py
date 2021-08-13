n = int(input())

a = [0 for _ in range(23)]

b = list(map(int, input().split()))

for i in range(n):
    a[b[i]-1] += 1

for i in a:
    print(i,end=' ')