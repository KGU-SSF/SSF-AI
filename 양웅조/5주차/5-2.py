line = int(input("몇 줄로 쌓을까요?")) #몇 줄로 쌓는지 알기 위해 int input
for x in range(1,line+1):
    print (" " * (line - x) + "* " * x) #앞에 공백은 위에서부터 순서대로 line에서 하나 씩 줄어드는 식으로 공백이 생겨서 line-x만큼 공백
