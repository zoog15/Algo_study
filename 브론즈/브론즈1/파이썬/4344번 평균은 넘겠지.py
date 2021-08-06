# 4344번 평균은 넘겠지 : https://www.acmicpc.net/problem/4344

import sys

tc = int(sys.stdin.readline())
result = []

for i in range(tc):
    score = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    avg = (sum(score) - score[0]) / score[0]
    for k in range(1, len(score)):
        if score[k] > avg:
           cnt += 1
    answer = cnt/(len(score)-1) * 100
    result.append(answer)

for i in result:
    print(f'{i:.3f}%')