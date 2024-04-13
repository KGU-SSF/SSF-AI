from collections import deque #deque 자료구조 활용
word=input("") #단어 입력받음

queue=deque(word) #큐에 word 문자열이 순서대로 저장됨
same=True #회문 함수를 참으로 설정

while len(queue)>1: #문자열의 길이가 1이상일 때 반복문
    if queue.popleft() != queue.pop(): #문자열의에서 사라진 제일 왼쪽 글자와 오른쪽 글자가 같이 않다면 회문 함수는 False가 되게 함
        same=False
        break

if same: #회문 함수가 참일 때 True 출력
    print("True")
else: #회문 함수가 거짓일 때 False 출력
    print("False")





