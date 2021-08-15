n = int(input())
cnt = 0

for i in range(n+1):
    if i % 10 == 1:
       cnt += 1

print(cnt)