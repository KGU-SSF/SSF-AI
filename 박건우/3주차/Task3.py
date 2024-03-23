# 1번 문제 
# a = 0 
# b = 0

# a,b = input('input your numbers').split()

# a=int(a)
# b=int(b)

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)




#2번 
# print('시험점수를입력')
# a = int(input('점수 ='))

# if a < 101:
#     if a >= 90 and a <=100:
#         print('A')
#     elif a >= 80 and a <=89:
#         print('B')

#     elif a >= 70 and a <=79:
#         print('C')  
    
#     elif a >= 60 and a <=69:
#         print('D')
    
#     elif a <= 59:
#         print('F')
# else:        
#     print('다시입력해주세요')




#3번 문제
# w = []
# m = input('입력 =')

# for i in range(len(m)):
#     if m[i] == "1":
#         a = m[i:len(m)-1]
#         break
# t = a.split(',')  
# for y in range(len(t)):
#     if int(t[y]) % 2 != 0:
#         w.append(int(t[y]))
# print(w)

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]


#4번 문제
cook = input('입력 =')
for k in range(len(cook)):
    if cook[k]=="[":
        p = cook[k+1:len(cook)-1]
        break
o = p.split(",")
print(len(o))


        


