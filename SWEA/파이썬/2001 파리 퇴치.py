T = int(input())  # 테스트 케이스

for tc in range(T):
    N, M = map(int, input().split())  # N:배열크기, M:파리채크기
    fly = [[0]*N for _ in range(N)]

    for i in range(N):
        fly[i] = list(map(int, input().split()))

    max_f = 0  # 파리잡기 최댓값

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_f = 0  # MxM 파리 잡는숫자
            for k in range(i, i+M):
                for l in range(j, j+M):
                    sum_f += fly[k][l]
            if sum_f > max_f:
                max_f = sum_f

    print(f'#{tc+1} {max_f}')