# 15596번 정수 N개의 합 : https://www.acmicpc.net/problem/15596

import sys

def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum


n = list(map(int, sys.stdin.readline().split()))
print(solve(n))