n = int(input())
answer = 0
count = 1
high = 1

while True:
    high += 6*(count-1)
    # print(high)
    if n <= high:
        answer = count
        break
    else:
        count += 1

print(answer)