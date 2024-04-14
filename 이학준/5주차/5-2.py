n = int(input("숫자를 입력하세요"))

for i in range(0,n+1,1):#(시작, 끝-1, 몇개씩 증가할지)
    for j in range(0,n-i,1):#공백이 n개부터 점점 줄어들어야 하므로 n-i로 작성했음
        print(" ",end="")
    for k in range(0,i,1):
        print("* ",end="")#end를 쓴 이유는 줄바꿈을 막기 위해서고
    print("")#한 줄이 끝나면 다음줄로 넘어가기 위해