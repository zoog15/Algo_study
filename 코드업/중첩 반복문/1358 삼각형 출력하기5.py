n = int(input())

for i in range(0,(n+1)//2):
    for k in range(i,(n+1)//2-1):
        print(" ", end='')
    for j in range(0,2*i+1):
        print("*", end='')
    print()