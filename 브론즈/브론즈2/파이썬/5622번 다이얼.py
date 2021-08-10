# 5622번 다이얼 : https://www.acmicpc.net/problem/5622

import sys

arr = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
ans = 0

word = list(sys.stdin.readline().strip())

for i in word:
    for j in range(0, len(arr)):
        if i in arr[j]:
            ans += j+2

print(ans+len(word))
