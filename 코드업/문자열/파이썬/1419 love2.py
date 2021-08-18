s = list(input())

cnt = 0

for i in range(len(s)-3):
    if s[i] == 'l' and s[i+1] == 'o' and s[i+2] == 'v' and s[i+3] == 'e':
        cnt += 1

print(cnt)