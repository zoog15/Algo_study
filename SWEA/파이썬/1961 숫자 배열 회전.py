# i=2-- j=0		i=2 j=2--		i=0++ j=2
#
# i=2-- j=1		i=1 j=2--		i=0++ j=1
#
# i=2-- j=2		i=0 j=2--		i=0++ j=0

T = int(input())  # 테스트 케이스

for tc in range(T):
    n = int(input())
    arr = [[0]*n for _ in range(n)]  # n*n 배열 생성, 처음에 1개씩 들어가있는
    arr2 = [[""]*n for _ in range(n)]  # 돌려진 값들이 들어갈 배열

    for i in range(n):
        arr[i] = list(map(int, input().split()))

    for i in range(n):
        for j in range(n):
            s = ""
            if j == 0:
                for k in range(n):
                    s += str(arr[n-k-1][i])
            if j == 1:
                for k in range(n):
                    s += str(arr[n-i-1][n-k-1])
            if j == 2:
                for k in range(n):
                    s += str(arr[k][n-i-1])
            arr2[i][j] = s

    print(f'#{tc+1}')
    for i in range(n):
        for j in range(n):
            print(arr2[i][j], end=' ')
        print()
