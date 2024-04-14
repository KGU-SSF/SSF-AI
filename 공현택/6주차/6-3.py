N=int(input()) #줄의 개수 입력
number=[] #number을 리스트로 정의해서 나중에 리스트 정렬할 때 사용할 예정
for i in range(N): #N번 입력해서 각각 number리스트에 추가하기
    num=int(input())
    number.append(num)
number.sort() #리스트 크기 순으로 정렬

print(" ") 
for i in range(len(number)): #리스트 크기만큼 반복해서 출력
    print(number[i])