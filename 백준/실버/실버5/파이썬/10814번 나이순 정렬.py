n = int(input())  # 입력받을 사람의 수
arr = []

for i in range(n):
    data = input().split()
    arr.append((int(data[0]), data[1]))

arr = sorted(arr, key=lambda x: x[0])

for i in range(n):
    print(arr[i][0],arr[i][1])