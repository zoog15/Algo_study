# 20492번 세금 : https://www.acmicpc.net/problem/20492

n = int(input())

a = 0.78 * n
b = (1-(0.2*0.22))*n

print(int(a), int(b))
