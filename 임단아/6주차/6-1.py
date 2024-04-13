#6주차 1번

words = ['level','rotator','hello' ]

for word in words:
    if list(word) == list(reversed(word)):     # 역순과 비교
        print(word, "TRUE")
    else:
        print(word, "FALSE")