import sys

a, b, c = map(str, sys.stdin.readline().split())
s = []

s.append(a)
s.append(b)
s.append(c)

s.sort()
print(s[0])
print(s[2])


