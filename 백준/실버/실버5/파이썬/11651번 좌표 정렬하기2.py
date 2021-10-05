n = int(input())
arr = []

for i in range(n):
    data = input().split()
    arr.append((int(data[0]), int(data[1])))

arr = sorted(arr, key = lambda x: (x[1], x[0]))

for i in range(n):
    print(*arr[i])