a, b = map(float, input().split())

c = []

c.append(a+b)
c.append(a-b)
c.append(b-a)
c.append(a*b)
c.append(a/b)
c.append(b/a)
c.append(pow(a,b))
c.append(pow(b,a))

print(format(max(c),".6f"))