n = int(input())
a = []

if n == 0:
    a.append(0)
while n != 0:
    a.append(n%2)
    n //= 2


l = len(a)
for i in range(l):
    print(a.pop(), end='')

