a=int(input("줄의 개수: "))  #줄의 개수 입력
b=[]                         #리스트를 만들기 위한 공백 리스트
c=[]                         #리스트를 만들기 위한 공백 리스트
for i in range(a):           #줄의 개수만큼 반복
    b.append(int(input()))   #입력한 수 b리스트로 삽입
b.sort()                #리스트 정렬
    
for i in b:          #b의 리스트 길이 만큼 반복
    if i not in c:   #b리스트 중 중복되는 값 제외하고 c리스트에 삽입
        c.append(i)
        
for i in range(len(c)):  #c리스트의 길이 만큼 반복
    print("정렬 결과:",c[i])          #c리스트의 값 하나씩 출력