import sys

# 유클리드 호제법
def GCD(a,b):
    if b == 0: return a
    return GCD(b, a%b)

# 최소공배수 = 두 수의 곱 / 최대공약수
def LCM(a,b):
    lcm = a*b//GCD(a,b)
    return lcm


a, b = map(int, sys.stdin.readline().split())
if b > a: a, b = b, a  # 더 큰수를 앞에 두기

print(GCD(a,b))
print(LCM(a,b))
