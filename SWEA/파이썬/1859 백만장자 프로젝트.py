# 앞에서부터의 최대값을 확인, 그 전까지의 인덱스를 최대값에서 빼서 이득에 더하기
# 최대값에 해당하는 index에 도착하면 그 뒤의 인덱스에서 다음 최대값 다시 찾아서 저장, 다시 반복
import copy
from collections import deque

T = int(input())  # 테스트 케이스 수

for i in range(T):
    n = int(input())  # 총 몇개 물건?
    a = list(map(int, input().split()))  # 각 물건의 매매가
    prof = 0  # 이득
    max_p = max(a)  # 처음 a에서의 최대값
    b = copy.deepcopy(a)
    b.sort(reverse=True)

    if a == b:  # 가격이 내림차순이라 아무것도 사지 않는것이 이득임
        print(f"#{i+1} {prof}")
        continue

    q = deque(a)
    while True:
        num = q.popleft()
        if len(q) == 0: break
        if num == max_p:  # num이 최대값에 도달했다면
            max_p = max(q)  # 남아있는 q에서의 최댓값
            continue
        prof += max_p - num  # 제일 처음에 들어온 값들을 배출하며 prof에 더해줌

    print(f"#{i+1} {prof}")