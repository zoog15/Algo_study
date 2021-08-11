# 11720번 숫자의 합 : https://www.acmicpc.net/problem/11720

import sys

n = sys.stdin.readline()
sum = 0
s = list(sys.stdin.readline().strip())

for i in s:
    sum += ord(i)-ord('0')

print(sum)
