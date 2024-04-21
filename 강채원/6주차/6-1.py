def is_palindrome(word):
    return word == word[::-1]#입력한 단어를 거꾸로 뒤집은 후(::-1) 원본 단어와 비교하여 회문인지의 여부를 판별함
word = input("단어를 입력하세요: ")
if is_palindrome(word):
        print("TRUE")
else:
        print("FALSE")