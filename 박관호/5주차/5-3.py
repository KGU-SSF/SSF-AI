import numpy as np
score_list = []

for i in range(1, 4):
    binary_list = list(map(int, input().split()))
    score_list.append(binary_list)
    
array_score = np.array(score_list)

for row in array_score:
    score = sum(row)
    if score == 4:
        print("E")
    elif score == 3:
        print("A")
    elif score == 2:
        print("B")
    elif score == 1:
        print("C")
    else :
        print("D")