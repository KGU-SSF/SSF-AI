import numpy as np  

input_data = np.array([3,5]) #값을 지정(바꿀 수 없음)

weight_hidden_0 = np.array([2,3]) #가중치 입력 
weight_hidden_1 = np.array([4,-5]) #가중치 입력 
weight_output = np.array([2,7])  #가중치 입력 

hidden_0_value = (input_data*weight_hidden_0).sum()   #(3x2)+(5x3) 행렬 계산 
hidden_1_value = (input_data*weight_hidden_1).sum()   #(3x4)+(5x-5) 행렬 계산 
print(hidden_0_value,hidden_1_value,sep=',') 

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]  # (21x2)+(-13x7) 
print(output)  #output 출력 