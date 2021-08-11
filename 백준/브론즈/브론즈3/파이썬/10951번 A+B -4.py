# 10951번 A+B -4 : https://www.acmicpc.net/problem/10951

import sys

answer = []

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        answer.append(a+b)
    except:
        break

for i in answer:
    print(i)