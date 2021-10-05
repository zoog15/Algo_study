n = int(input())  # 입력받을 사람의 수
arr = [0] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))
    arr[i].append(1)

for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            arr[i][2] += 1

for i in range(n):
    print(arr[i][2], end=' ')