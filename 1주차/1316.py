def solution(N):
    group = 0  # 그룹 단어의 개수

    for i in range(N):
        word = input()
        group_word = True  # 그룹단어인지 판별
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:  # 연속된 문자가 다를 때
                if word[i] in word[i + 1:]:  # 현재 문자가 뒤에 또 나오면 그룹 단어가 아님
                    group_word = False
                    break
        if group_word:
            group += 1

    return group


N = int(input())
print(solution(N))
