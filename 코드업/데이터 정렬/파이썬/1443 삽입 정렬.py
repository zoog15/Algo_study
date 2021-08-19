n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(1,n):
    key = a[i]
    j = i-1
    while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

for i in range(n):
    print(a[i], end=' ')