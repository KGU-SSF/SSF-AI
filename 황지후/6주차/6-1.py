inp = list(input("단어를 입력하시오 : "))#회문일지 판단할 단어 받기

N = len(inp)
T = 1
if N == 1:#한글자인 경우 무조건 대칭이므로 True를 출력하도록 하기
    T = 0

for i in range (int(N/2)):#단어가 대칭인지 판단하기
    if inp[i] == inp[N - i - 1]:
        T = 0
    else:
        T = 1
        break


print (T == 0)#True 또는 False 출력하기
