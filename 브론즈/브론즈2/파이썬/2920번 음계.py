# 2920번 음계 : https://www.acmicpc.net/problem/2920

import sys

n = list(map(int, sys.stdin.readline().split()))
flag = 0

for i in range(0, len(n)-1):
    if n[0] == 1 and (n[i] + 1 == n[i+1]):
        flag += 1
    elif n[0] == 8 and (n[i] - 1 == n[i+1]):
        flag += 2
    else:
        flag = 0

if flag == 7:
    print("ascending")
elif flag == 14:
    print("descending")
else:
    print("mixed")
