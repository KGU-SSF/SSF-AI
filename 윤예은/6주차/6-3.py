from collections import deque
n=int(input()) #앞으로 몇 줄을 출력할지 정수 입력받음

num=deque() #데크를 사용해 num에 수열을 순서대로 입력함
for _ in range(n):#n번 숫자 입력
    number=int(input())

    if number in num: #입력한 숫자가 앞에 입력했던 수와 같다면 오류 메세지를 출력하고 프로그램 종료
        print('수가 중복되지 않아야 합니다.')
        exit()
    num.append(number) 

for i in range(1, len(num)): #리스트 두 번째 수부터 마지막 숫자까지 반복함
    pon=num[i] #현재 반복중인 숫자를 pon변수에 저장
    j=i-1 #pon숫자의 바로 이전 위치의 인덱스를 j에 저장함
    while j>=0 and num[j]>pon:#pon숫자가 이전 숫자보다 작을 때까지 반복함
        num[j+1]=num[j] #이전 숫자를 한 칸 뒤로 옮겨 빈 공간을 만듦
        j-=1 #j를 한 칸 왼쪽으로 이동해 이전 숫자와 다음 숫자를 비교함
    num[j+1]=pon #이전 숫자보다 작은 pon 숫자를 빈 공간에 넣어 정렬함

print("")

for i in num: #정렬된 수를 반복해 한 줄에 하나씩 출력함
    print(i)