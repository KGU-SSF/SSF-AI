k=int(input()) #줄의 개수 설정
num=[] #리스트 선언

for i in range(k): 
    d=int(input()) #k번 입력
    if d==0: 
        del num[-1] #0이면 맨 뒤에있는 리스트값 지우기 
    else:
        num.append(d) #그게 아니라면 그값 리스트에 추가!
        
print(sum(num)) #리스트의 합 구해서 나타내기
