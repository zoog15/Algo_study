# 4153번 직각삼각형 : https://www.acmicpc.net/problem/4153

while True:
    a = list(map(int, input().split()))
    max_a = max(a)
    a.remove(max_a)
    if sum(a) == 0: break
    if a[0]**2 + a[1]**2 == max_a**2:
        print("right")
    else:
        print("wrong")