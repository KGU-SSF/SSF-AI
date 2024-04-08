arrs = [[], [], []]
counts = [0, 0, 0]

def printCount(counts):
    for i in range(3):
        if (counts[i] == 3):
            print("A")
        elif (counts[i] == 2):
            print("B")
        elif (counts[i] == 1):
            print("C")
        elif (counts[i] == 4):
            print("E")
        elif (counts[i] == 0):
            print("D")

for i in range(3):
    a = list(map(int, input().split())) # 여러개의 값을 공백으로 나누어 입력받아 a 리스트에 저장
    arrs[i] = a[:] # arr[i]에 a 리스트 복사
    for j in range(len(a)):
        if (a[j] == 1):
            counts[i] = counts[i] + 1

printCount(counts)

