list = []

a = int(input("원하는 갯수 :"))

for i in range(a):
    b = int(input())
    list.append(b)

list.sort()

for j in range(a):
    print(list[j])