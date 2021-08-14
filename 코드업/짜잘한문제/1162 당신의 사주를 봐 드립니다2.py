y, m, d = map(int, input().split())

ans = ((y+m+d)//100)%10

if ans % 2 == 0:
    print("대박")
else:
    print("그럭저럭")

