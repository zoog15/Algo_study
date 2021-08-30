N = int(input())  # 사람 수
p = list(map(int, input().split()))

p.sort()
sum_p = 0

for i in range(N):
    for j in range(0,i+1):
        sum_p += p[j]

print(sum_p)