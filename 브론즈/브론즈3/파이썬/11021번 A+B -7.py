# 11021번 A+B -7 : https://www.acmicpc.net/problem/11021

tc = int(input())
arr = []

for i in range(tc):
    a, b= map(int, input().split())
    arr.append(a+b)

for i in range(1, len(arr)+1):
    print(f"Case #{i}: {arr[i-1]}")