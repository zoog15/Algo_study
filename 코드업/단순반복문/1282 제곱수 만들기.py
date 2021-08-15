n = int(input())
i = 1

for i in range(1, n+1):
    if i*i <= n < (i+1)*(i+1):
        k = n-i*i
        t = i
        break

print(k,t)
