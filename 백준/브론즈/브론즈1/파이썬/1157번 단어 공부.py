# 1157번 단어 공부 : https://www.acmicpc.net/problem/1157

s = input().upper()
words = list(set(s))  # 중복된 문자들 다 없애고 list로 만듬
cnt_list = []

for x in words:  # 각 문자가 몇번 나왓는지 확인함
    cnt = s.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:  # cnt_list 안에서 최댓값이 같은게 여러개면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  # cnt_list에서 최댓값의 index 반환
    print(words[max_index])
