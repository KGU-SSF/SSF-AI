#문제1
A,B=input().split()
A,B=int(A),int(B)
print(A+B, A-B, A*B, A//B, A%B)

#문제2
a=int(input())
if a>100 or a<0: print('다시 입력해주세요')
elif a>=90: print('A')
elif a>=80: print('B')
elif a>=70: print('C')
elif a>=60: print('D')
else: print('F')

#문제3
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[0:1]+nums[2:3]+nums[4:5]+nums[6:7]+nums[8:9])

#문제4
cook=["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소세지", "라면", "팥빙수", "김치전"]
print(len(cook))