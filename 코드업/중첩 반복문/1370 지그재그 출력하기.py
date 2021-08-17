h, r = map(int, input().split())

while r != 0:
    for i in range(0, h):
        for j in range(0, i):
            print(" ", end = '')
        print("*")
    for i in range(h-1,0,-1):
        for j in range(0,i-1):
            print(" ", end='')
        print("*")
    r -= 1