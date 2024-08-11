N = int(input()) #단어 수
count = 0 #그룹단어 수


for _ in range(N):
    word = input() #N개만큼 단어 입력
    previous_letter = [] #전에 나온 알파벳을 저장하는 곳
    group_word = "1"

    for i in range(len(word)): 
        if word[i] in previous_letter: #알파벳이 이미 전에 나온 알파벳일 때
            if word[i] != word[i-1]: # 이전 글자와 다를 때
                group_word = "0" # 그룹단어가 아님.
        else:
            previous_letter.append(word[i]) #전에 나온 알파벳에 추가
    
    if group_word == "1":
        count += 1

print(count)
