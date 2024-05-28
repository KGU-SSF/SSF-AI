import numpy as np 

input_data = np.array([3,5]) #입력 값
weight_hidden_0 = np.array([2,3]) #입력값 가중치
weight_hidden_1 = np.array([4,-5]) #입력값 가중치 
weight_output = np.array([2,7]) #출력값 가중치
#행렬곱 연산
hidden_0_value = (input_data * weight_hidden_0).sum()
hidden_1_value = (input_data * weight_hidden_1).sum()
print(hidden_0_value, hidden_1_value, sep=',')

output = hidden_0_value * weight_output[0]+hidden_1_value*weight_output[1]
print(output)