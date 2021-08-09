# 10809번 알파벳 찾기 : https://www.acmicpc.net/problem/10809

import sys

word = [0 for _ in range(26)]
flag = [0 for _ in range(26)]

s = list(sys.stdin.readline().strip())

for i in range(0, len(s)):
    word[ord(s[i])-97] = s.index(s[i])  # 순번에 해당하는 위치에 index값 넣기
    flag[ord(s[i])-97] = 1  # 있는 글자들은 flag on

for i in range(0, len(word)):
    if flag[i] == 0:
        word[i] = -1

for i in word:
    print(i, end=' ')
