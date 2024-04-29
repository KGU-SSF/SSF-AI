Word = input("단어를 입력하세여~")
N = len(Word) -1  #Word 의 인덱스는 0 부터 시작이므로 -1 을 해야 범위 오류가 나지 않습니다!
num = 0   # True 이니 아닌지 확인 용도로 쓰이는 변수
for i in range(N):             
    if Word[i] == Word[N-i]:
        pass
    else:
        num +=1        # 일치 하지 않으면 num 수를 증가시킴
if num == 0:        
    print("True")
else:
    print("False")
