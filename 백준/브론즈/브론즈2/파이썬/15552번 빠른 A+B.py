# 15552번 빠른 A+B : https://www.acmicpc.net/problem/15552

# import sys 하고 input 들어가던 자리에 sys.stdin.readline()만 해주면됨. 하지만 전부 문자열이니 형변환 알아서 잘 할 것
import sys

n = int(sys.stdin.readline())
answer = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    answer.append(a+b)

for i in answer:
    print(i)
