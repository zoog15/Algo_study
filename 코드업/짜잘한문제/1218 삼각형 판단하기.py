a = list(map(int, input().split()))

a.sort()

if a[2] < a[0] + a[1]:
    if a[0] == a[1] ==  a[2]:
        print("정삼각형")
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        print("이등변삼각형")
    elif a[0]**2 + a[1]**2 == a[2]**2:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")