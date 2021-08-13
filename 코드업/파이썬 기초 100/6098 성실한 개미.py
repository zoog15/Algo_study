d = []

for i in range(10):
    d.append(list(map(int, input().split())))

x = 1
y = 1

while True:
    if d[x][y] == 2:
        d[x][y] = 9
        break
    else:
        d[x][y] = 9
    if d[x][y+1] == 0 or d[x][y+1] == 2:
        y += 1
    else:
        x += 1
    if x==8 and y ==8:
        d[x][y] = 9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()