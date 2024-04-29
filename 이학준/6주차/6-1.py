def is_palindrome(word):  
    if word == word[::-1]:  #문자열을 역순으로 반환
        return True         #함수 반환
    else:
        return False

while True:
    word = int(input("단어를 입력하세요")) 
    
    if is_palindrome(word):  
        print("True") 
    else:
        print("False")  