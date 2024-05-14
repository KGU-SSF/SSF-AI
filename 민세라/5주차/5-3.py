li = list(map(int,input().split(' ')))
cnt = 0

for i in li:
    if(i==1):
        cnt+=1
        
if(cnt==1):
    print('A')
elif(cnt==2):
    print('B')
elif(cnt==3):
    print('C')
elif(cnt==4):
    print('D')
else:
    print('E')