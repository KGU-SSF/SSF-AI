N = int(input("줄의 길이를 정하시오 : "))#줄의 길이 입력받기
list_a = []#빈 리스트 만들기

for i in range(N):
    list_a.append(int(input("{}번째 숫자를 입력하시오 : ".format(i + 1))))#리스트에 숫자 입력받기

list_a.sort()#리스트를 오름차순으로 정렬하기
list_a = set(list_a)#중복되는 값 지우기
list_a = list(list_a)#set을 리스트로 변환하기

for i in range(len(list_a)):#리스트 안의 값을 한줄씩 출력하기
    print (list_a[i])