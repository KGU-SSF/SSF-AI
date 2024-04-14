N = int(input("줄의 길이를 정하시오 : "))#줄의 길이 입력받기
list_a = []#빈리스트 만들기


for i in range(N):
    inp = (int(input("{}번쨰 값을 입력하시오  : ".format(i+1))))
    if inp == 0 and len(list_a) > 0:#입력받은 값이 0일때 마지막 값 지우기
        list_a.remove(list_a[-1])

    else:
        list_a.append(inp)#0이 아니라면 리스트에 값 추가하기

result = 0

for i in list_a:#리스트 값의 합 구하기
    result += i

print (result)