a = list(map(int, input().split()))
cnt = 0

for i in a:
    if i <= 170:
        print("CRASH",i)
        break
    else:
        cnt += 1

if cnt == 3:
    print("PASS")