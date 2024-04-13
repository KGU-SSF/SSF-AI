#6주차 3번

n = int(input("숫자를 입력하시오. : "))   #값 입력
num_list=[]
for i in range(n):
    num_list.append(int(input()))   #값 입력을 반복
num_list.sort()
for i in range(n):
    print(num_list[i])  #입력한 값을 오름차순으로 정렬하여 출력