while True:
    n, m = map(int, input().split())
    if 2 <= n <= 9 and 2 <= m <= 9:
        break
    else:
        print("INPUT ERROR!")

for i in range(1, 10):
    if n < m:
        for j in range(n, m+1):
            print(j,"*",i,"=",format(j*i,"2d"),end='   ')
    else:
        for j in range(n, m-1, -1):
            print(j, "*", i, "=", format(j * i, "2d"), end='   ')
    print()

