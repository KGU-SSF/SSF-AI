n=int(input())#n을 사용자에게 입력받기
num_list=[]
for i in range(n):#0부터 n-1까지 반복하기
    num_list.append(int(input()))#사용자로부터 입력받은후 num_list 에 추가
num_list.sort()#오름차순으로 정렬
for i in range(n):#0부터 n-1까지 반복
    print(num_list[i])