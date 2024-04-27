num = int(input())
 
num_list = []
 
for i in range(num):
    a = int(input())
    num_list.append(a)
 
num_list.sort()
 
for i in num_list:
    print(i)
 