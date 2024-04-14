a=int(input('숫자를 입력하세요'))#숫자 입력받기
for i in range(1,a+1):
    for j in range(0,a-i):#빈칸 생성
        print(' ',end='')
    for k in range(0,i):#*을 줄 수만큼 출력
        print('* ',end='')
    print('')
  