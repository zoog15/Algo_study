# 17496번 스타후르츠 : https://www.acmicpc.net/problem/17496

import math
n, t, c, p = map(int, input().split())

if not n%t:
    day = n/t-1
else:
    day = math.floor(n/t)

print(int(day*c*p))

