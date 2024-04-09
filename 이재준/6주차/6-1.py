def name(word):
    return word == word[::-1] #문자열과 뒤집은 문자열이 같은가?

def check(word):
    if name(word):
        print("True")     #같다
    else:
        print("False")   #아니다

word = input("입력 예시: ")
check(word)
