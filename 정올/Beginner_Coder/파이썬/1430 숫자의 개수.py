import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

flag = [0]*10

answer = a*b*c

while answer != 0:
    mod_n = answer%10
    flag[mod_n] += 1
    answer //= 10

for i in range(len(flag)):
    print(flag[i])