def is_palindrome(w):       #회문인지 판단하는 함수를 입력받는다
    return w == w[::-1]

a = ["level", "rotator", "hello"]  #단어를 입력받는다

for w in a:
    print(is_palindrome(w)) #회문인지 여부를 판단한다