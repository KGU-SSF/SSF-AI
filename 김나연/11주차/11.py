import numpy as np  

input_data = np.array([2,3]) #지정된 값 바꿀 수 없음 

weight_hidden_0 = np.array([1,1]) 
weight_hidden_1 = np.array([-1,1])  
weight_output = np.array([2,-1])   

hidden_0_value = (input_data*weight_hidden_0).sum()
hidden_1_value = (input_data*weight_hidden_1).sum()
print(hidden_0_value,hidden_1_value,sep=',')

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]
print(output)