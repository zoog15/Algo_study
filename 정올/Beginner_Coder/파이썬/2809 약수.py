import math
import sys

n = int(sys.stdin.readline())
sq = math.sqrt(n)
arr = []

for i in range(1, int(sq)+1):
    if n % i == 0:
        arr.append(i)
        if n//i not in arr:
            arr.append(n//i)

arr.sort()

for i in arr:
    print(i, end=' ')
