#6주차 1번

words = ['level','rotator','hello' ]    # 단어출력

for word in words:
    if list(word) == list(reversed(word)):     # 역순 비교하기
        print(word, "TRUE")     # 역순이면 true출력
    else:
        print(word, "FALSE")    #역순이 아니면 false출력