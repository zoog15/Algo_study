import math

A, B, V = map(int, input().split()) # A: 낮에 올라가는 거리, B: 밤에 미끄러지는 거리, V: 나무높이

if A >= V:
    day = 1
else:
    day = math.ceil((V-A)/(A-B))+1

print(day)
