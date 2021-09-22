import sys


def GCD(a,b):
    if b == 0: return a
    return GCD(b, a%b)


# 최소공배수 = 두 수의 곱 / 최대공약수
def LCM(a,b):
    lcm = a*b//GCD(a,b)
    return lcm


n = int(sys.stdin.readline())  # 입력받을 정수 갯수
a = list(map(int, sys.stdin.readline().split()))

gcd = lcm = a[0]
for i in range(1,n):
    gcd = GCD(gcd,a[i])
    lcm = LCM(lcm,a[i])

print(gcd, lcm)
