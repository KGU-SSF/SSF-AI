list1 = input("회문입력:")

for i in range(0,len(list1)): # 리스트의 길이만큼 반복
    if list1[i] == list1[-1-i]: # 회문인지 비교
        a = True # 회문이라면 True
    else:
        a = False 
print(a)
        