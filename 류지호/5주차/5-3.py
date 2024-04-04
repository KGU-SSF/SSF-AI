a=input().split()       #공백을 기준으로 입력받기
if a.count("1")==0:     #1의 개수에 맞는 알파벳 출력
    print("D")
if a.count("1")==1:
    print("C")
if a.count("1")==2:
    print("B")        
if a.count("1")==3:
    print("A")
if a.count("1")==4:
    print("E")    