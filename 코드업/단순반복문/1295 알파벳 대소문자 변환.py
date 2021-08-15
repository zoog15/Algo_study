s = input()
ans = []

for i in range(0, len(s)):
    if 97 <= ord(s[i]) <= 122:
        ans.append(s[i].upper())
    elif 65 <= ord(s[i]) <= 90:
        ans.append(s[i].lower())
    else:
        ans.append(s[i])

for i in ans:
    print(i, end='')