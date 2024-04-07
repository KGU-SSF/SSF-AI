matrix = []
rows=3
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for yuts in matrix:
    count = yuts.count(0)  
    if count == 1:
        print("A") 
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
    else:
        print("E")