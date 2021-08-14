kal = 0
n, m = map(int, input().split())

if n == 1:
    kal += 400
elif n == 2:
    kal += 340
elif n == 3:
    kal += 170
elif n == 4:
    kal += 100
else:
    kal += 70

if m == 1:
    kal += 400
elif m == 2:
    kal += 340
elif m == 3:
    kal += 170
elif m == 4:
    kal += 100
else:
    kal += 70

if kal > 500:
    print("angry")
else:
    print("no angry")