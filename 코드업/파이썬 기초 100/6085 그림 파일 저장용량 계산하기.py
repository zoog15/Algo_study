a, b, c = map(int, input().split())

ans = float(a*b*c)/8/1024/1024

print(format(ans, ".2f"),"MB")