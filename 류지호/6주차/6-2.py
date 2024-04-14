a=int(input("줄의 개수: "))    #줄의 개수입력
b=[]                          #리스트를 만들기 위한 공백 리스트
for i in range(a):            #줄의 개수만큼 반복하여 b리스트에 삽입
    b.append(int(input()))   
    if b[-1]==0:              #리스트 마지막에 0이 들어오면 0삭제
        b.remove(b[-1])
        for i in range(b.count(b[-1])): #0앞에 있는 값을 그 값의 수만큼 삭제
            b.remove(b[-1])
    elif b[-1]>9 or b[-1]<0:   #값이 0~9사이에 있는게 아니면 삭제
        b.remove(b[-1])
print("총합 :", sum(b))        #리스트에 있는 값 다 더하기