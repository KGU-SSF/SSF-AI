a=list(input("글자입력: "))   #리스트로 글자입력받기
if a==list(reversed(a)):     #리스트를 뒤집은것과 같으면 Ture 아니면 False 출력
    print("True")
else:
    print("False")    