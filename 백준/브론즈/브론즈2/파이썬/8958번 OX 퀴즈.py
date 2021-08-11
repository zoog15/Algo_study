# 8958번 퀴즈 : https://www.acmicpc.net/problem/8958

import sys

tc = int(sys.stdin.readline())
answer = []

for i in range(tc):
    str = input()
    cnt = 0;
    sum = 0;
    for j in range(0, len(str)):
        if str[j] == 'X':
            cnt = 0
            continue
        cnt += 1
        sum += cnt
    answer.append(sum)

for i in answer:
    print(i)
