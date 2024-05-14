q = []                  #q 배열 선언
k = int(input())        #입력 받을 개수 k

for i in range(0,k):    #0부터 k만큼 반복
    qu = int(input())   
    if(qu!=0):          # qu != 0 
        q.append(qu)    # qu가 0이 아닐 때 q 안에 qu 값을 넣음
    else :
        q.pop()         #qu가 0일 때에는 q 배열 안에 가장 최근에 넣은 값을 빼버림.

result = sum(q)         #파이썬 안에 있는 sum() 내장함수를 이용해서 q 배열 안에 있는 값을 전부 더함.
print(result)