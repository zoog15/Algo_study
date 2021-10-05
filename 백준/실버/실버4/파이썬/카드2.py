from collections import deque

n = int(input())
arr = []

for i in range(1, n+1):
    arr.append(i)

queue = deque(arr)

while len(queue) != 1:
    queue.popleft()  # 맨 왼쪽걸 뺴버림
    queue.append(queue.popleft())  # 그다음 맨 왼쪽껄 빼서 오른쪽에 추가

print(*queue)
