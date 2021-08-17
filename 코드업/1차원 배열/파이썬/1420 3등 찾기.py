n = int(input())
name = []
score = []
s = []

for i in range(n):
    a, b = input().split()
    name.append(a)
    score.append(int(b))

for i in range(n):
    s.append(score[i])
s.sort()

print(name[score.index(s[len(s)-3])])  # 이게 3등