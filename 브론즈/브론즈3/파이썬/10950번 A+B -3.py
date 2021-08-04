# 10950번 : A+B -3 : https://www.acmicpc.net/problem/10950

tc = int(input())

answer = []

for i in range(tc):
    a, b = map(int, input().split())
    answer.append(a+b)

for i in answer:
    print(i)