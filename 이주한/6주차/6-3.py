num = []

n = int(input("개수 :"))

for i in range (0, n) :
    temp = int(input("수 입력 : "))
    num.append(temp)


num_list = list(set(num))
num_list.sort()

for i in num_list :
    print(i)
