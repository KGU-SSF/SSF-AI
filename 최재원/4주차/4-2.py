num = []
num = input("리스트 데이터를 입력하세요. :").split()

#.split는 입력 받은 값 공백
#input은 문자열을 할당 받는 것이므로 int 로 형변환 시켜주어야 한다.
#map은 리스트의 각 원소를 정수로 바꾸어주는것

for i in num:
    print(i)