loop = int(input())

numlist = []
for i in range(0,loop):
    numadd = int(input())
    if numadd != 0:
        numlist.append(numadd)
        print("!=0")
    else:
        if len(numlist) > 0:
            del numlist[-1]
        
print(sum(numlist))
        