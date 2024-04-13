n = int(input())   # 수의 개수를 입력받는다
num_list=[]        # 수를 저장할 리스트 
for i in range(n):
  num_list.append(int(input()))    # 리스트에 수 추가
num_list.sort()                    # 오름차순 정렬 
for i in range(n):
  print(num_list[i])