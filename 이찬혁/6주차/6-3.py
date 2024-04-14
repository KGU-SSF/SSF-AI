numOfint = int(input())
numList = []
for i in range(0,numOfint):
    numList.append(int(input()))
numList.sort()
for i in numList:   
    print(i)