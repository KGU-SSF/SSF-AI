def palindrome(word):
    word = word.lower()  # 입력된 단어를 소문자로 변환
    return word == word[::-1] #입력된 단어와 그 단어를 뒤집었을 때가 같은지를 비교합니다. 


input_word = input("단어를 입력하세요: ")


if palindrome(input_word):
    print(f"{input_word} 회문입니다.")
else:
    print(f"{input_word} 회문이 아닙니다.")


