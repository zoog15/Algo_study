# 10871번 X보다 작은 수 : https://www.acmicpc.net/problem/10871

import sys

n, x = map(int, sys.stdin.readline().split())  # n : 정수 갯수, X : 기준이될 수

sm = list(map(int, sys.stdin.readline().split()))

for i in sm:
    if i < x:
        print(i, end=' ')
