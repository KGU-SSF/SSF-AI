import numpy as np

input_data = np.array([3,5]) #입력 데이터를 [3,5]로 설정

weight_hidden_0 = np.array([2,3]) #각 층의 가중치를 설정 [2,3]
weight_hidden_1 = np.array([4,-5]) #각 층의 가중치를 설정 [4,-5]
weight_output = np.array([2,7]) #각 층의 가중치를 설정 (weight_hidden_0 의 가중치는 2, weight_hidden_1의 가중치는 7)

hidden_0_value = (input_data * weight_hidden_0).sum() #입력 데이터와 가중치를 곱한 후 각각의 값을 계산 (3 * 2) + (5 * 3) = 21
hidden_1_value = (input_data * weight_hidden_1).sum() #입력 데이터와 가중치를 곱한 후 각각의 값을 계산 (3 * 4) + (5 * -5) = -13
print(hidden_0_value,hidden_1_value,sep=',') # 위의 값들을 출력

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #value값과 가중치를 곱하고 더해서 최종 출력 계산
print(output) #최종 값 출력