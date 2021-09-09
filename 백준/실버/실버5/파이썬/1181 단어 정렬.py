# 단어 정렬 : https://www.acmicpc.net/problem/1181

import sys

n = int(sys.stdin.readline())  # 입력 횟수
set_s = set()  # 중복된 문자는 출력 안할거니 애초에 set 으로 선언

for i in range(n):
    set_s.add(sys.stdin.readline().strip())  # set 안에 값 넣어주기

list_s = list(set_s)

list_s.sort()
list_s.sort(key = len)

for i in list_s:
    print(i)