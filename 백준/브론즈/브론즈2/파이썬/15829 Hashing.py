# 15829번 Hashing : https://www.acmicpc.net/problem/15829

import sys

a = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
answer = 0

for i in range(a):
    answer += ((ord(s[i])-ord('a')+1) * 31**i)

print(answer%1234567891)
