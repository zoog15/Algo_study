from collections import deque
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
cd = deque(c)

for i in range(b):
    d = cd.popleft()
    if d in a:
        print("1", end=' ')
    else:
        print("0", end=' ')
