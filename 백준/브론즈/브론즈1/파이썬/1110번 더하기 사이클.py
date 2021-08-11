# 1110번 더하기 사이클 : https://www.acmicpc.net/problem/1110

import sys

n = int(sys.stdin.readline())
first = n
cnt = 0

while True:
    a = n // 10
    b = n % 10
    s = a+b
    if s>=10:
        s -= 10
    n = (b*10)+s
    # print("n :", n)
    cnt += 1
    if n == first:
        break

print(cnt)
