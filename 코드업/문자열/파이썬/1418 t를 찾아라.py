s = input()
a = []

for i in range(len(s)):
    if s[i] == 't':
        a.append(i+1)

for i in a:
    print(i, end=' ')