import numpy as np

input_data=np.array([3,5]) #입력 값 정의

weight_hidden_0=np.array([2,3]) #입력 값에 대한 가중치 [2,3]
weight_hidden_1=np.array([4,-5]) #두 번째 입력값에 대한 가중치 [4,5]
weight_output=np.array([2,7]) #2는 weight_hidden_0의 가중치, 7은 weight_hidden_1의 가중치


hidden_0_value=(input_data*weight_hidden_0).sum() # 3*2 + 5*3 = 21
hidden_1_value=(input_data*weight_hidden_1).sum() # 3*4 + 5*(-5) = -13
print(hidden_0_value,hidden_1_value,sep=',') # 21, -13 출력

output=hidden_0_value*weight_output[0] + hidden_1_value*weight_output[1] #두 value 값과 가중치(weight_output)값을 곱한 후 더함
print(output) # output = 21*2 + (-13)*7 = -49. -49 출력
