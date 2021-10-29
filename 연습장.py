import math


def comb(a,b):
    result = math.factorial(b) // (math.factorial(b-a) * math.factorial(a))
    return result


tc = int(input())  # 테스트 케이스

for i in range(tc):
    a, b = map(int, input().split())
    print(comb(a, b))