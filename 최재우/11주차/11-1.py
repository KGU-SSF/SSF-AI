import numpy as np #넘파이 받아오기 

input_data = np.array([3, 5]) #초기 입력값 정의

weight_hidden_0 = np.array([2, 3]) #1번째 입력값 가중치
weight_hidden_1 = np.array([4, -5]) #2번째 입력값 가중치
weight_output = np.array([2, 7]) #hidden_0의 가중치가 전자, hidden_1의 가중치가 후자

hidden_0_value = (input_data * weight_hidden_0).sum() #계산 값은 21
hidden_1_value = (input_data * weight_hidden_1).sum() #계산2 값은 -13
print(hidden_0_value, hidden_1_value, sep=",") #위의 계산값 2개 출력

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #value와 가중치값을 계산
print(output) #최종결과 -49 출력