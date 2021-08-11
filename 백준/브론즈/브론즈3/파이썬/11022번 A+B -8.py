# 11021번 A+B -7 : https://www.acmicpc.net/problem/11021

tc = int(input())
arr = []
ar = []
br = []

for i in range(tc):
    a, b= map(int, input().split())
    ar.append(a)
    br.append(b)
    arr.append(a+b)

for i in range(1, len(arr)+1):
    print(f"Case #{i}: {ar[i-1]} + {br[i-1]} = {arr[i-1]}")