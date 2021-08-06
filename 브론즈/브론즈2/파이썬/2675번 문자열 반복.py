# 2675번 문자열 반복 : https://www.acmicpc.net/problem/2675

import sys

tc = int(sys.stdin.readline())

for i in range(tc):
    txt = ''
    n, s = input().split()  # 굳이 n을 int로 바꿀 필요는 없음 split을 기준으로 n과 s받기
    for r in s:
        txt += int(n) * r
    print(txt)

