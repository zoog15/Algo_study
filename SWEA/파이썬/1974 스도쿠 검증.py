#  행별로 확인, 열별로 확인, 3x3씩 확인하기
# 00 03 06 30 33 36 60 63 66
T = int(input()) # 테스트 케이스

for tc in range(T):
    sudo = [[0]*9 for _ in range(9)]  # 9x9 배열로 테스트 케이스마다 초기화
    chk = [0 for _ in range(9)] # 1~9까지 숫자들이 나왔는지 체킹용
    ans = 1  # 스도쿠에 문제없음

    for i in range(9):
        sudo[i] = list(map(int, input().split()))  # 각 행별로 입력

    for i in range(9):  # 오른쪽으로 확인
        sum1 = 0
        sum2 = 0
        for j in range(9):
            sum1 += sudo[i][j]  # 오른쪽으로 확인
            sum2 += sudo[j][i]  # 아래로 확인
        if sum1 != 45 or sum2 != 45:  # 좌우 합이 45가 아니면 중단!
            ans = 0
            break

    for j in range(0,6,3):  # 3x3씩 확인
        for k in range(0,6,3):
            sum3 = 0
            r = j+3
            c = k+3
            for l1 in range(j,r):
                for l2 in range(k,c):
                    sum3 += sudo[l1][l2]
            if sum3 != 45:
                ans = 0
                break

    print(f'#{tc+1} {ans}')

    # for i in range(9):  # 잘 들어와있는지 확인용
    #     for j in range(9):
    #         print(sudo[i][j], end=' ')
    #     print()