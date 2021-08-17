n = int(input())

for i in range(0, n):
    if i == 0 or i == n-1 or i == n//2:
        for j in range(0, n):
            print("*", end='')
    else:
        for k in range(0, n):
            if k == 0 or k == n-1 or k == i or k == n-i-1 or k == n//2:
                print("*", end='')
            else:
                print(" ", end='')
    print()