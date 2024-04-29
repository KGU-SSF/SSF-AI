#변수선언
tmp = []
real_list = []
cnt = 0
result = {0:"E",1:"A",2:"B",3:"C",4:"D"}

#3회 결과 저장
for i in range(3):
  tmp = list(map(int,input().split()))
  real_list.append(temp)

#3회 결과 출력. 배(0)와 등(1)을 기준으로

for i in range(3):
  cnt = real_list[i].count(0)
  print(result.get(cnt))
