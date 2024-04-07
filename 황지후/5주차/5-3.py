#윷 정보를 받아와 공백을 기준으로 각 값으로 나눠 리스트에 넣기
pla_list = map(int, input("윷 정보를 입력하시오 : ").split())
pla_list = list(pla_list)
pla_sum = 0
#0 과 1로 저장된 윷의 상태를 모두 더하기
for i in range(4):
    pla_sum += pla_list[i]

#윷의 상태를 더한 값을 바탕으로 족보에 따라 결과 내보내기
if pla_sum == 3:
    print ("A")
elif pla_sum == 2:
    print ("B")
elif pla_sum == 1:
    print ("C")
elif pla_sum == 0:
    print ("D")
else:
    print ("E")