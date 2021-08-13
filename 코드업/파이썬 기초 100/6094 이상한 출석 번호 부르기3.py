a = int(input())

b = list(map(int, input().split()))

min = b[0]

for i in b:
    if i < min:
        min = i

print(min)