n = int(input())  # 찾으려는 분수의 순서

if n == 1:
    x = 1
    y = 1
else:
    size = 1

    while n -size > 0:
        n -= size
        size += 1

    # print(n, temp, size)

    if size % 2 == 0:
        x = 1
        y = size

        for i in range(n-1):
            x += 1
            y -= 1
    else:
        x = size
        y = 1

        for i in range(n-1):
            x -= 1
            y += 1

print(str(x)+"/"+str(y))







