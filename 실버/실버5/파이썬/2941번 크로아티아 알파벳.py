# 2941번 크로아티아 알파벳 : https://www.acmicpc.net/problem/2941

import sys

s = sys.stdin.readline().strip()

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    s = s.replace(i, "a")  # s에 a의 각 값들이 있다면 a 한글자로 변환시켜버림

print(len(s))
