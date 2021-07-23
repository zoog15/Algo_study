n = int(input())

a = []

a.append(0)
a.append(1)
a.append(1)

for i in range(3, (n+1)):
    a.append(a[i-2]+a[i-1])

print(a[n])
