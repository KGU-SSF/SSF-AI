K = int(input("내려놓을 카드의 개수를 입력하세요:"))
list = [] #입력받은 숫자를 list함수에 저장

for _ in range(K): #숫자를 K번 입력받음
    i = int(input())
    if i ==0:
        list.pop() #입력받을 값이 0이라면 가장 최근에 말한 숫자를 지우기 위해 list.pop을 사용했다.
    else:
        list.append(i) #0이 아니면 리스트에 저장
total = sum(list)
print(total)