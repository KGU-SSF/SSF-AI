##1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.##
jjaksu=[]

for i in range(99):
    if((i%2)==0):
        jjaksu.append(i)
        
jjaksu = tuple(jjaksu)
print(jjaksu)
    