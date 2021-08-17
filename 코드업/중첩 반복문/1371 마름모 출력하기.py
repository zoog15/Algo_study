n = int(input())

for i in range(0, n):
    for j in range(i, n-1):
        print(" ", end='')
    print("*", end='')
    for k in range(0, i*2):
        print(" ", end='')
    print("*")
for i in range(n-1, -1, -1):
    for j in range(i, n-1):
        print(" ", end = '')
    print("*", end='')
    for k in range(0, i*2):
        print(" ",end = '')
    print("*")