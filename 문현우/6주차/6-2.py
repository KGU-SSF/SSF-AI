from collections import deque #deque는 큐 와 스택의 특성 모두 갖고 있음 이 문제는 큐,스택 둘다 사용가능!
#이 문제에서 중요한거는 같은수가 무한대로 나올수 있다이고 0이 포함되지 않고 1~9여야지 문제가 성립된다 그래야 0일때 틀렸다 판단하고 바로 직전 맞춘수를 뺄수있음
import random #1~9 랜덤 수가 나와야하기 때문
number=int(input("몇개의 수를 입력받을지:"))
qeue=deque()
for _ in range(number): #입력받은 수만큼 지속
    answer=int(input("수 입력:"))
    card=random.randint(1,2)
    if answer==card:
        qeue.append(card)
    else:
        print("0") #먼저 0을 보여줘야함
        if qeue: #이전 큐에 없을 경울 대비!
            qeue.pop()
print(sum(qeue))