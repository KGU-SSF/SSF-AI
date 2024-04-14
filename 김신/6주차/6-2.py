k = int(input()) #받을 수의 개수 정하기
add = []
for i in range(1,k+1):
    num = int(input()) #k번 수 입력
    if num != 0 :
        add.append(num) #0이 아니면 받은 수 리스트에 추가
    elif num == 0 :
        add.pop() #0이면 지우기
print(sum(add)) #add리스트에 있는 수 모두 합산