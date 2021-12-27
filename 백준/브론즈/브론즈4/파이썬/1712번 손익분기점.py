# a : 고정비용, b: 인건비, c : 판매액
a, b, c = map(int, input().split())

profit = c - b

if profit <=0:
    print(-1)
else:
    print(a//profit+1)

