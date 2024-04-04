pla_list = map(int, input("윷 정보를 입력하시오 : ").split())
pla_list = list(pla_list)
pla_sum = 0
for i in range(4):
    pla_sum += pla_list[i]

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