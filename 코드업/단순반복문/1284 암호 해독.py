n = int(input())
a = []
cnt2 = 0

for i in range(2, n+1):
    cnt = 0
    if n % i == 0:
        for j in range(2, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            a.append(i)
            cnt2 += 1
    if cnt2 == 2:
        break

if len(a) == 1:
    if a[0] * a[0] == n:
        print(a[0], a[0])
    else:
        print("wrong number")
elif len(a) == 2:
    if a[0] * a[1] == n:
        print(a[0], a[1])
    else:
        print("wrong number")
else:
    print("wrong number")
