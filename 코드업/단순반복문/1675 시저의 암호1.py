s = input()
ans = []

for i in range(0, len(s)):
    if s[i] == " ":
        ans.append(" ")
    elif ord(s[i])-3 < 97:
        ans.append(chr(120-97+ord(s[i])))
    else:
        ans.append(chr(ord(s[i])-3))

for i in ans:
    print(i, end='')