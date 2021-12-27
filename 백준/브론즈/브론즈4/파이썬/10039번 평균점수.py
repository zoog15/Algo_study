score = []

for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    score.append(a)

print(sum(score)//5)