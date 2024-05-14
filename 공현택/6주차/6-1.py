for p in range(3): #3번 반복해서 입력 받을 코드
    result = "True" #result 선언 및 초기화
    a=input("단어 입력 : ")
    for i in range((len(a)//2)+1): #a문자열 길이의 절반만큼 반복
        if a[i]!=a[-i-1]: #가장 끝에 있는거부터 차례대로 비교
            result="False" #만약 다르다면 result 값을 False로 초기화
            break

    if result =="True": 
        print("True") 
    else: 
        print("False")