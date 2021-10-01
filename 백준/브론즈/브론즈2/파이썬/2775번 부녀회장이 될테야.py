tc = int(input())

for testCase in range(tc):
    k = int(input())  # 살려는 층
    n = int(input())  # 살려는 호
    arr = [[0]*n for _ in range(k+1)]
    for i in range(n):
        arr[0][i] = i+1

    for i in range(1,k+1):
        for j in range(n):
            for l in range(j+1):
                arr[i][j] += arr[i-1][l]

    print(arr[k][n-1])
