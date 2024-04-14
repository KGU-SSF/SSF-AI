num_value = int(input("수를 입력하세요"))
num_list = []

for i in range(num_value) : 
    num = int(input())
    num_list.append(num)
    
num_list.sort()
    
print(num_list)