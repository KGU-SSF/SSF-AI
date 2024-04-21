a = input ("단어를 입력하세요")

if a == a[::-1] : #a에 담긴 단어와 이를 뒤집었을 때 같다면 True 출력
    print ("True")
else :
    print ("False")