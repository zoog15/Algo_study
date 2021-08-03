# 2439번 별 찍기 2 : https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(i+1):
        print("*", end='')
    print()