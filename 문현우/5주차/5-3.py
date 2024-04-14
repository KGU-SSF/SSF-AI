jul = [input().split() for i in range(3)] #리스트 컴프리헨션 사용

for p in jul:
    bae = p.count('1')  #배 수  count사용하여 list 안의 갯수 카운트
    deong = p.count('0')  #등 수
    if bae==0:
        print("D") #윷
    elif bae==1:
        print("A") #도
    elif bae==2:
        print("B") #개
    elif bae==3:
        print("C") #걸
    elif bae==4:
        print("E") #모