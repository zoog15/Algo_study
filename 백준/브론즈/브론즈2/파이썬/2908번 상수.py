# 2908번 상수 : https://www.acmicpc.net/problem/2908

import sys

a, b = sys.stdin.readline().split()

r_a = a[::-1]  # 거꾸로 만들어서 저장하기
r_b = b[::-1]

if r_a > r_b:
    print(r_a)
else:
    print(r_b)

