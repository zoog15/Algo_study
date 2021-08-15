a, b, c, d = map(int, input().split())

ab = float(a/b)
cd = float(c/d)

if ab > cd:
    print(">")
elif ab < cd:
    print("<")
else:
    print("=")