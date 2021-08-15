s = input()
ans = []

for i in range(0, len(s)):
    if s[i] == " ":
        ans.append(" ")
    elif ord(s[i])+3 > 122:
        ans.append(chr(97+abs(ord(s[i])-120)))
    else:
        ans.append(chr(ord(s[i])+3))

for i in ans:
    print(i, end='')