'''
push_front x : 정수 x를 덱의 앞에 넣기
push_back x : 정수 x를 덱의 뒤에 넣기
pop_front : 덱의 가장 앞에 있는 수 빼고 출력, 없으면 -1
pop_back : 덱의 가낭 맨 뒤에 있는 수 뺴고 출력, 없으면 -1
size : 덱에 들어있는 정수 개수 출력
empty : 덱이 비어있으면 1, 아니면 0
front : 덱의 가장 앞에 있는 정수 출력, 없으면 -1
back : 덱의 가장 뒤에 있는 정수 출력, 없으면 -1
'''
import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        deque.reverse()
        deque.append(order[1])
        deque.reverse()
    if order[0] == 'push_back':
        deque.append(order[1])

    if order[0] == 'pop_front':
        if len(deque):
            deque.reverse()
            print(deque.pop())
            deque.reverse()
        else:
            print(-1)
    if order[0] == 'pop_back':
        if len(deque):
            print(deque.pop())
        else:
            print(-1)

    if order[0] == 'size':
        print(len(deque))
    if order[0] == 'empty':
        if len(deque):
            print(0)
        else:
            print(1)

    if order[0] == 'front':
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(deque):
            print(deque[-1])
        else:
            print(-1)


