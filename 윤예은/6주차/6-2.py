from collections import deque
k=int(input()) #정수를 입력받음

num=deque() #데크를 사용해 num에 수열을 입력함
for _ in range(k): 
    number=int(input()) #k번 수를 입력함

    if number==0: #입력한 수가 0이라면 num수열에서 최근에 입력됐던 수가 삭제됨
        num.pop()
    else: #0이 아니라면 num 수열에 추가됨
        num.append(number)

print(sum(num)) #삭제되고 남은 수를 모두 더한 값 출력