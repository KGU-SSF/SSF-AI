num1=input("단어를 입력하시오:")
list1=list(num1)
list1_reverse=list(reversed(list1)) #list1_reverse변수에 입력된 문자열을 reversed()함수를통해 거꾸로 저장

if list1 == list1_reverse:  #입력받은 문자열과 거꾸로 된 문자열을 비교
    print("TRUE")
else:
    print("FALSE")