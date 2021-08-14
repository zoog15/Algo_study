s = input()

a1, b = s.split(" ")
a2 = int(a1[:2])

if b == '1' or b == '2':
    ans = 2012 - 1900 - a2 +1
    print(ans)
else:
    ans = 2012 - 2000 - a2 +1
    print(ans)