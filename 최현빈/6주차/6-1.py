word = input("단어를 입력하시오: ")
is_palindrome = True                         #초기 팰린드롬 값을 True로 설정
for i in range(len(word)//2):                #입력된 단어의 절반까지만 반복
    if word[i] != word[-1 - i]:              #문자의 대칭이 안 맞는 경우
        is_palindrome = False                #팰린드롬 아닌 것으로 판단하여 False로 설정
print(is_palindrome)                         #결과값 출력