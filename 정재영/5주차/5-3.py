results = []
for _ in range(3):
    result = input().split()
    count = result.count('1')
    results.append(count)

for result in results:
    if result == 0:
        print('D') 
    elif result == 1:
        print('C')  
    elif result == 2:
        print('B')  
    elif result == 3:
        print('A')  
    elif result == 4:
        print('E')