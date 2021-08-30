N, M, L = map(int, input().split())  # N:사람수, M:던질때 몇칸씩, L:한사람이 몇번받으면 끝?

cnt_a = [0] * N  # 각 인원당 공 몇번 받았는지 체크
cnt_a[0] = 1  # 1번부터 공을던지니 이미 1번 잡은상태로 시작
cnt = 0  # 총 공이 몇번 왓다갓다하는지 확인
ball = 0  # 지금 공이 누구에게 있는지

while True:
    if cnt_a[ball] % 2 == 1:  # 홀수번 잡았으면
        ball += L  # 시계방향으로
        if ball >= N:  # N번 넘어서는 다시 처음부터
            ball -= N
    elif cnt_a[ball] % 2 == 0:
        ball -= L  # 반시계방향
        if ball < 0:
            ball += N
    cnt_a[ball] += 1  # 공 잡은횟수 늘려주기
    cnt += 1  # 총 공 움직인 횟수 올려주기
    if cnt_a[ball] == M:
        break

print(cnt)
