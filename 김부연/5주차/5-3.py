for i in range(3):# 세명의 결과 받기 위해 반복문 설정 
    a = list(map(int, input("0 또는 1을 입력하세요(0:배,1:등): ").split()))#split 함수 사용해서 공백포함해서 입력가능하게 함 0과 1문자열로 입력한거 정수형으로 바꿔줌 map함수 0 갯수 세기 위해 사용
    while not all(x in [0, 1] for x in a):#a에 0과 1이 없으면 계속 입력할 수 있도록 무한 반복문 이용 0과 1이 있는지 확인하는 거는 all 함수
        print("다시 입력해주세요:")
        a = list(map(int, input("0 또는 1을 입력하세요(0:배,1:등): ").split()))# 0과 1 제외한 다른 숫자 입력했을 떄 다시 입력하게 해줌 all함수 사용 
        
    

    if a.count(0) == 1:#도
        print("A")
    elif a.count(0) == 2:#개
        print("B")
    elif a.count(0) == 3:#걸
        print("C")   
    elif a.count(0) == 4:# 윷
        print("D")
    else:
        print("E")#모