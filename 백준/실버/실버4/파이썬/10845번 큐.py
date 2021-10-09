'''
push x : 정수 x를 큐에 넣음
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력, 만약 큐에 들어있는 정수 없으면 -1
size : 큐에 들어있는 정수 개수
empty : 큐가 비어잇으면 1, 아니면 0
front : 큐의 가장 앞에 있는 정수 출력, 없으면 -1
back : 큐의 가장 뒤에 있는 정수 출력, 없으면 -1
'''
import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        queue.append(order[1])
    if order[0] == 'pop':
        if len(queue):
            queue.reverse()
            print(queue.pop())
            queue.reverse()
        else:
            print(-1)
    if order[0] == 'size':
        print(len(queue))
    if order[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    if order[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)