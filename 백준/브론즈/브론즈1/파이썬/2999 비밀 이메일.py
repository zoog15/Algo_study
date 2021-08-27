# 2999번 비밀 이메일 : https://www.acmicpc.net/problem/2999
import math

s = list(input())

gizun = int(math.sqrt(len(s)))  # 제곱수를 넘어가면 r>=c 가 되기때문에 제곱수 아래까지만 확인하면됨

r = 1; c = 1;


for i in range(1, gizun+1):
    for j in range(1, len(s)+1):
        if i*j == len(s):
            r = i
            c = j

arr = [[0]*c for _ in range(r)]  # rxc 크기의 배열 생성
cnt = 0


for i in range(c):
    for j in range(r):
        arr[j][i] = s[cnt]
        cnt += 1

for i in range(r):
    for j in range(c):
        print(arr[i][j], end='')