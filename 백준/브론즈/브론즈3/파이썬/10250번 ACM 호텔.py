testcase = int(input())  # 테스트 케이스 수

for tc in range(testcase):
    h, w, n = map(int, input().split())  # hxw 크기의 호텔, n번째 손님
    count = 0  # 지금이 몇번째 방이기 체크하기 위한 카운트

    for i in range(1,w+1):
        for j in range(1,h+1):
            count += 1
            if count == n:  # n번째 손님에게 배정받을 방
                # 문자열로 바꿔서 층수+방순서 연결
                if i < 10:  # 10보다 작을때는 앞에 0을 붙여줘야함 -> 4층의 2번째방 -> 402번
                    answer = str(j) + "0" + str(i)
                else:
                    answer = str(j) + str(i)

    print(answer)