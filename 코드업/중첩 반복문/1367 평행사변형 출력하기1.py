n = int(input())

for i in range(0, n):
    for j in range(i, n-1):
        print(" ", end='')
    for k in range(0, n):
        print("*", end='')
    print()