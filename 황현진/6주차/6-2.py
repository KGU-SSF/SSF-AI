a = int(input("적을 수의 개수를 정하세요")) #입력받을 숫자의 개수를 입력받는다
number = []
zero = []
result = 0
for i in range(0, a):                     #반복문을 이용하여 a번 만큼 b의 값을 입력받고 만약 b가 0이 아니라면 
    b = int(input())                      #number 리스트에 값을 넣고 0이라면 가장 최근에 입력받은 값을 제거한다 
    if b!=0:
        number.append(b)
    if b == 0:
        number.pop()
result = sum(number)                      #이후 number리스트에 있는 모든값을 더한뒤 결과값으로 출력하고 프로그램을 종료시킨다
print(result)
