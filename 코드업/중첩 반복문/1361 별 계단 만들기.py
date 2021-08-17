n = int(input())

for i in range(0, n):
    for j in range(0,i):
        print(" ", end='')
    for k in range(0,2):
        print("*", end='')
    print()