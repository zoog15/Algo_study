n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for i in a:
    print(i, end=' ')

# 파이썬은 그냥 sort() 메서드 쓰자