import sys


n, k = map(int, sys.stdin.readline().split())
arr = []
count = 0

for i in range(n):
    arr.append(int(sys.stdin.readline()))


for i in range(len(arr)):
    mok = k // arr[len(arr)-1-i]
    count += mok
    k -= arr[len(arr)-1-i] * mok

print(count)