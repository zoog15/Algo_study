a = list(map(int, input().split()))
cnt = 0

for i in  a:
    if i == 1:
        cnt += 1

if cnt == 0:
    print("모")
elif cnt == 1:
    print("도")
elif cnt == 2:
    print("개")
elif cnt == 3:
    print("걸")
else:
    print("윷")