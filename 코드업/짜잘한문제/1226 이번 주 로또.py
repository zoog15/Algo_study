a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
bonus = 0

for i in range(len(a)-1):
    for j in range(len(b)):
        if b[j] == a[i]:
            cnt += 1

for i in b:
    if i == a[len(a)-1]:
        bonus += 1

if cnt == 6:
    print("1")
elif cnt == 5 and bonus == 1:
    print("2")
elif cnt == 5:
    print("3")
elif cnt == 4:
    print("4")
elif cnt == 3:
    print("5")
else:
    print("0")
