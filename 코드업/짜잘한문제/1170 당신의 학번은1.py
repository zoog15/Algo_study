a, b, c = map(str, input().split())

if len(c) == 1:
    c = '0'+c

print(a+b+c)