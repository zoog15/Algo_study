# 거꾸로 전부 0으로 만들어버리기?
# 제일 처음 1이 나왓을때부터 0으로 바꾸고, 그 뒤에를 반대 숫자로 바꿈
# 0000이 될때까지 반복
T = int(input())  # 테스트 케이스
cnt = 0

for i in range(T):
    cnt = 0
    s = list(input())  # 원래의 메모리 상태

    for j in range(len(s)):
        if s[j] == '0': continue  # 값이 0이면 일단 패스
        else:  # 값이 1일때
            s[j] = '0'  # 1을 0으로 바꿈
            for k in range(j+1, len(s)):  # 그 뒤 인덱스부터 값을 반대로 바꿈
                if s[k] == '0':
                    s[k] = '1'
                else:
                    s[k] = '0'
            # print(s)
            cnt += 1
            if '1' not in s:
                break

    print(f'#{i+1} {cnt}')


