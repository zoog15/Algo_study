H, K, d = map(str, input().split())

h = int(H)
k = int(K)

for i in range(0, h):
    if d == 'R':
        for j in range(i, h-1):
            print(" ", end='')
        for l in range(0, k):
            print("*", end='')
    elif d == 'L':
        for j in range(0, i):
            print(" ", end='')
        for l in range(0, k):
            print("*", end='')
    print()
