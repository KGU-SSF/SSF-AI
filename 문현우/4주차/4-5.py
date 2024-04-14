even_list=[]
for i in range(2,100,2):
    even_list.append(i)
print(tuple(even_list))
"""공백이 발생하는데 end=""를 쓰려하니 안되었음 이유가 end=""는 한줄에 
출력이 끝나고 마지막에 추가되는 문자열을 지정하는데 사용되기때문 이때문에
tuple을 사용해서 요소로 바뀌었기때문"""