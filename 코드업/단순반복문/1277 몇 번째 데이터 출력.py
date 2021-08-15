n = int(input())

cen = n//2

a = list(map(int, input().split()))

print(a[0], a[cen], a[len(a)-1])