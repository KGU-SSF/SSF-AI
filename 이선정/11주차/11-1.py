import numpy as np

Input_data = np.array([3,5]) # 입력 값을 정의하는 부분

weight_hidden_0 = np.array([2,3]) # 입력 값에 대한 가중치 ([2,3])
weight_hidden_1 = np.array([4,-5]) # 두 번째 입력 값에 대한 가중치 ([4,-5])
weight_output = np.array([2,7]) # 2 : weight_hidden_0의 가중치, 7 : weight_hidden_1의 가중치

hidden_0_value = (Input_data*weight_hidden_0).sum() # 계산 3*2+5*3 = 21
hidden_1_value = (Input_data*weight_hidden_1).sum() # 계산 3*4+5*-5 = -13
print(hidden_0_value, hidden_1_value, sep=',') # 위 계산 결과에 따라 21, -13이 출력됨

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] # 두 value 값과 가중치 (weight_output) 값을 곱한 후 ㅓ함
print(output) # 21*2 + (-13)*7 = -49이므로 -49가 출력됨 