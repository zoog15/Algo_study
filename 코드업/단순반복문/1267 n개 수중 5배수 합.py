n = int(input())
a = list(map(int, input().split()))
sum = 0

for i in a:
    if i % 5 == 0:
        sum += i

print(sum)