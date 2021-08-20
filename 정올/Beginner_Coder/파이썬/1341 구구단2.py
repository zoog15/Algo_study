n, m = map(int, input().split())

if n <m:
    for a in range(n, m+1):
        num = 1
        for i in range(1, 4):
            for j in range(1, 4):
                print(a,"*",num,"=",format(a*num,"2d"), end='   ')
                num += 1
            print()
        print()
else:
    for a in range(n, m-1, -1):
        num = 1
        for i in range(1, 4):
            for j in range(1, 4):
                print(a, "*", num, "=", format(a * num, "2d"), end='   ')
                num += 1
            print()
        print()
