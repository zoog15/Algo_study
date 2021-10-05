from sys import stdin as st

n = int(st.readline())
arr = [0] * 10001

for i in range(n):
    num = int(st.readline())
    arr[num] += 1

for i in range(10001):
    while arr[i]:
        print(i)
        arr[i] -= 1