n, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == 1) or (i == n) or (j == 1) or (j == n):
            print('*', end='')
        elif (i+j-1) % k == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()