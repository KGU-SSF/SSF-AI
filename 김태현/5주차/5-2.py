num=int(input()) #피라미드 높이 입력

for i in range(1, num + 1): #공백을 고려하여 1부터 num+1 까지 반복
        print(" " * (num - i) +"* " * i)  #공백과 별을 횟수에 맞게 출력
        


