from collections import deque 

def palindrome(s):  # palindrome 함수를 정의한다. 이 함수는 문자열 s를 받아 회문인지를 판별
    
    queue = deque()  # deque 객체를 생성
    
    for x in s:  # 입력받은 문자열 s의 각 문자에 대해 반복
        
        if x.isalpha():  # 현재 문자가 알파벳 문자인지 확인
            queue.append(x.lower())  # 알파벳 문자라면, 소문자로 변환한 후 deque의 오른쪽 끝에 추가
    
    while len(queue) > 1:  # deque의 길이가 1보다 큰 동안 반복
        if queue.popleft() != queue.pop():  # deque의 왼쪽 끝과 오른쪽 끝에서 각각 하나씩 문자를 꺼내서 비교
            return False  # 두 문자가 다르다면, 주어진 문자열은 회문이 아니므로 False를 반환

    return True  # 모든 비교에서 문자가 일치했다면, 문자열은 회문이므로 True를 반환

word = input("판별할 단어를 입력하세요.")  # 사용자로부터 문자열을 입력받음

print(palindrome(word))  # 입력받은 문자열이 회문인지를 판별하는 함수를 호출하고, 결과를 출력
