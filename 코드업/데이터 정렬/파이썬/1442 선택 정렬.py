n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(n):
    min = i
    for j in range(i+1,n):
        if a[j] < a[min]:
            min = j
    temp = a[i]
    a[i] = a[min]
    a[min] = temp

for i in range(n):
    print(a[i], end=' ')