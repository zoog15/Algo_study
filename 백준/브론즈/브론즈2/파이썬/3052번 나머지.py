# 3052번 나머지 : https://www.acmicpc.net/problem/3052

import sys

arr = []
cnt = 1

for i in range(10):
    n = int(sys.stdin.readline())
    mod = n % 42
    arr.append(mod)

arr.sort() # 중복 없애기 위해 정렬

for i in range(9):  # 앞 뒤가 서로 다르면 갯수를 올리고 다음꺼부터 진행, 이렇게 해야 중복 안됨
    if arr[i] != arr[i+1]: 
        cnt += 1
        continue

print(cnt)