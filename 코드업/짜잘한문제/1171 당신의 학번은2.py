a, b, c = map(str, input().split())

if len(b) < 2:
    b = '0' + b

if len(c) == 1:
    c = '00' + c
elif len(c) == 2:
    c = '0' + c

print(a+b+c)