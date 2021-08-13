a, b, c, d = map(int, input().split())

ans = float(a*b*c*d)/8/1024/1024

print(format(ans, ".1f"),"MB")