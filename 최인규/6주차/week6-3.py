n = int(input())
 
n_list = [] 
 
for i in range(n): 
    a = int(input()) 
    n_list.append(a) 
 
n_list.sort() # n_list를 오름차순으로 정렬
 
for i in n_list: 
    print(i) 
