def is_palindrome(w):       #is_palindrome이라는 함수 설정
    w = w.lower().replace(" ", "")   #문자열w를 모두 소문자로 변경하고 공백 제거
    return w == w[::-1]           #바뀐w가 뒤집힌 w와 같은지 비교 [::-1]은 문자열을 뒤집기 위해 있음

input = input("문장을 입력하세요: ")   
if is_palindrome(input):          #회문인지 확인
    print("true")
else:
    print("false")