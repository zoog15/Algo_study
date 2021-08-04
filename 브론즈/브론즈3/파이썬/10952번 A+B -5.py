# 10952번 A+B -5 : https://www.acmicpc.net/problem/10952

import sys

arr = []

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    arr.append(a+b)

for i in arr:
    print(i)