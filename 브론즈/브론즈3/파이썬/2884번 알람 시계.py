# 2884번 알람 시계 : https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())

if m < 45:
    m = 15 + m
    h -= 1
else:
    m = m - 45

if h < 0:
    h = 24 + h

print(h, m)

