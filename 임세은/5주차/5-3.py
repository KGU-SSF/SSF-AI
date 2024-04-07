arr = [[0] * 4 for _ in range(3)]   #3행 4열의 배열 선언 및 초기화

for i in range(3):
    arr[i]=list(map(int,input().split()))   #split를 사용하여 4개의 값입력받기

result=[0]*3    #결과를 입력할 배열 선언 및 초기화

for i in range(3):  #result배열에 arr 각행의 값을 저장
    for k in range(4):
        result[i]+=arr[i][k]

for i in range(3):  #result배열의 값에 따른 결과값 출력0
    if result[i]==0:
        print("D")

    elif result[i]==1:
        print("C")

    elif result[i]==2:
        print("B")

    elif result[i]==3:
        print("A")

    elif result[i]==4:
        print("E")