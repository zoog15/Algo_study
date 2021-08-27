n, m = map(int, input().split())

a = list(map(int, input().split()))

tri_sum = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            l = a[i]+a[j]+a[k]
            if l == m:
                tri_sum = m
                break
            elif l < m:
                if l > tri_sum:
                    tri_sum = l

print(tri_sum)

