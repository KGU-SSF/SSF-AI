num=int(input("개수N: "))
alist=[]

for i in range(num):
    a=int(input())
    alist.append(a)
alist2=alist.sort()

print("출력:")
for k in alist:
    print(k)
