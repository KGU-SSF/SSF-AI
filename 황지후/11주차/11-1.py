import numpy as np #넘파이 넣기

input_data = np.array([3,5])#3과 5를 가지를 행렬 만들기

weight_hidden_0 = np.array([2,3])#가중치로 사용할 2, 3 행렬 만들기
weight_hidden_1 = np.array([4,-5])#가중치로 사용할 4, -5행렬 만들기
weight_output = np.array([2,7])#가중치로 사용할 2, 7 행렬 만들기

hidden_0_value = (input_data * weight_hidden_0).sum()# 기존의 행렬에 첫번쨰 가중치를 곱하여 더하기
hidden_1_value = (input_data * weight_hidden_1).sum()# 기존의 행렬에 두번째 가중치를 곱하여 더하기
print(hidden_0_value, hidden_1_value,sep=', ')#계산 후 나온 값을 출력하기

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] # 계산 후 나온 행렬에 세번쨰 가중치를 곱하여 더하기
print(output) #결과값 출력