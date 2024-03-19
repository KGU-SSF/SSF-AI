print("리스트 요소 개수를 입력해주세요")
size = int(input())
print("값들을 입력해주세요")
cook = []

for i in range(0,size):
    cook.append(input()) 


print("리스트 요소 개수 ")
print(len(cook))