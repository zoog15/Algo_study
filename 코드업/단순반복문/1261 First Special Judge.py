a = list(map(int, input().split()))
cnt = 10

for i in a:
    if i % 5 == 0:
        print(i)
        break
    else:
        cnt -= 1

if cnt == 0:
    print("0")