n = int(input())   #리스트의 길이 설정
num_list=[]        #num_list 설정
for i in range(n):    #n만큼 반복하여 정수 입력
  num_list.append(int(input()))   #입력된 정수를 num_list에 추가
num_list.sort()                   #오름차순으로 설정 
for i in range(n):     #n에 대해 반복
  print(num_list[i])  