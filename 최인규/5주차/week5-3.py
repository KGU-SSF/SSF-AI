for i in range(3):
    # 사용자로부터 입력받은 값을 공백을 기준으로 분리하고, 정수형으로 변환하여 a 리스트에 저장
    a = list(map(int, input().split()))
    
    # 0의 개수가 1개일 경우 'A'를 출력 (도)
    if a.count(0) == 1: 
        print("A")
        
    # 0의 개수가 2개일 경우 'B'를 출력 (개)
    elif a.count(0) == 2: 
        print("B")
    
    # 0의 개수가 2개일 경우 'C'를 출력 (걸)
    elif a.count(0) == 3: 
        print("C")
    
    # 0의 개수가 2개일 경우 'D'를 출력 (윷)
    elif a.count(0) == 4: 
        print("D")
    
    # 0이 없을 경우 'E'를 출력 (모)
    else: 
        print("E")
