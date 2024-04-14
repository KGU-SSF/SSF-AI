def name(word):
    return word == word[::-1] #문자열과 뒤집은 문자열이 같은지 확인하는 함수,[::-1]은 문자열을 거꾸로 뒤집는 역할을 한다.

def check(word):         #word가 회문인지 확인해보자
    if name(word):        
        print("True")     #같다
    else:
        print("False")   #아니다

word = input("입력 예시: ") #문자열 입력받기
check(word)
