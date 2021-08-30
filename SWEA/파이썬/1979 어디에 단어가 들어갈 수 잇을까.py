T = int(input())  # 테스트 케이스 수


for tc in range(1, T+1):
    N, K = map(int, input().split())  # 퍼즐길이, 단어길이
    puzzle = [[0]*N for _ in range(N)]  # NxN 크기 생성
    cnt_a = 0  # 들어갈수있는 칸이 몇개인지
    check = [[0] * N for _ in range(N)]

    for i in range(N):
        puzzle[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 0: continue  # 막혀잇으면 바로바로 패스
            elif puzzle[i][j] == 1:  # 흰칸이면
                x = i
                y = j
                cnt_D = 0  # 아래 확인
                cnt_R = 0  # 오른쪽확인
                while True:  # 아래으로 확인
                    if check[x-1][j] == 1:
                        break
                    if x >= N or puzzle[x][j] == 0:
                        # print(i,j,"에서 아래확인 :",cnt_D)
                        if cnt_D == K:
                            cnt_a += 1
                        break  # 퍼즐범위를 벗어나거나 0을 만나면 멈춰
                    x += 1
                    cnt_D += 1
                while True: # 오른쪽으로 확인
                    if check[i][y-1] == 1:
                        break
                    if y >= N or puzzle[i][y] == 0:
                        # print(i,j,"에서 오른쪽확인 :",cnt_R)
                        if cnt_R == K:
                            cnt_a += 1
                        break  # 퍼즐범위를 벗어나거나 0을 만나면 멈춰
                    y += 1
                    cnt_R += 1
                check[i][j] = 1
    print(f'#{tc} {cnt_a}')