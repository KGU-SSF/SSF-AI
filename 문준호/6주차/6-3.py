num = int(input()) # 6입력받음
lis = list()


for _ in range(num): 
    x = int(input())
    for i in range(len(lis)+1):
        if i == len(lis):
            lis.append(x)
            break
        elif x > lis[i]:
            continue
        else:
            lis.insert(i, x)
            break

print(lis)