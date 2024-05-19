import numpy as np

input_data = np.array([3,5])    #입력 값을 정의하는 부분

weight_hidden_0 = np.array([2,3])   #입력 값에 대한 가중치 [2,3]
weight_hidden_1 = np.array([4,-5])  #두 번째 입력값에 대한 가중치 [4,-5]
weight_output = np.array([2,7])    #2는 weight_hidden_0의 가중치 7은 weight_hidden_1의 가중치 

hidden_0_value = (input_data * weight_hidden_0).sum() #게산 : 3 x 2 + 5 x 3 = 21
hidden_1_value = (input_data * weight_hidden_1).sum() #계산 : 3 x 4 + 5 x -5 = -13
print(hidden_0_value, hidden_1_value, sep = ",")    # 위 계산 결과의 따라 21, -13이 출력되어짐.

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #두 value 값과 가중치(weith_output)값을 곱한 후 더한다.
print(output)       # 따라서 ouput = 21 x 2 + (-13) x 7 = -49 이므로 -49가 출력되어짐.