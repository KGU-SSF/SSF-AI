K = int(input())
a =[]
index=0 # 인덱스 번호 저장 , 따로 인덱스 번호를 세지 않으면 for 문에서 에러남
for i in range(K):

    b = int(input())
    if b == 0:
        del a[index-1]    # 문제 조건에 0 앞에 지울수 있는 수가 보장 되어 있음
        index -= 1        #수 한개가 삭제 되었으므로 인덱스도 1 감소 
    else:
        a.append(b)     
        index += 1

    
print(sum(a))