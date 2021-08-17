def swap(a):
    temp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[-1] = temp


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(len(a)):
        print(a[j], end=" ")
    print()
    swap(a)
