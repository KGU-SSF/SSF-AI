#반복문 사용
word = input("단어를 입력하세요: ") #단어 입력받기

def is_palindrome(word):  #회문함수 선언/변수word
    for i in range(len(word) // 2): #변수 word의 길이의 절반만큼 반복
        if word[i] != word[-i-1]: #문자를 오른쪽과 왼쪽 비교 
            is_palindrome = False
            break
        
print("is_palindrome")

from collections import deque

def is_palindrome(word):
    chars = deque(word)
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


