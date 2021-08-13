a = int(input())

b = list(map(int, input().split()))

for i in reversed(b):
    print(i,end=' ')