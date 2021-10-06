from collections import deque


n, k = map(int, input().split())  # n: 인원수, k : 몇번째 사람 제거
arr = []
answer = []

for i in range(1, n+1):
    arr.append(i)

queue = deque(arr)

while queue:
    queue.rotate((-1*k)+1)
    answer.append(queue.popleft())

print('<'+str(answer)[1:-1] + '>')