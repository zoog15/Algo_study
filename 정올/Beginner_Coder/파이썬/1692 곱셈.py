import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
answer = a*b
while b != 0:
    mod_b = b % 10
    print(a*mod_b)
    b //= 10

print(answer)

