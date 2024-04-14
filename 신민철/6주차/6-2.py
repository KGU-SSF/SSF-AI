K = int(input("정수 입력:")) 
Q = [] 

for i in range(K):
    Q.append(int(input())) # 리스트에 요소 추가
    if Q[i] == 0: # 0 추가하면 0이랑 최근 요소 제거
        Q.pop()
        Q.pop()
result = sum(Q) # 리스트 합
print(result)
    

   
    