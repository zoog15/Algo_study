h, m = map(int, input().split())

if m < 30:
    if h == 0:
        h = 23
    else:
        h -= 1
    m += 30
else:
    m -= 30

print(h, m)