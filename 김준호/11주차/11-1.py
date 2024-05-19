import numpy as np

input_data = np.array([3,5]) # 초기 array 입력

weight_hidden_0 = np.array([2,3]) # 0번 hidden 노드의 가중치
weight_hidden_1 = np.array([4,-5]) # 1번 hidden 노드의 가중치
weight_output = np.array([2,7]) # output 노드 가중치

hidden_0_value = (input_data * weight_hidden_0).sum() # hidden_0 노드 계산
hidden_1_value = (input_data * weight_hidden_1).sum() # hidden_1 노드 계산
print(hidden_0_value, hidden_1_value, sep=",") # hidden layer의 노드 값 출력

# 기존에 알던 행렬곱이 아님 주의, 콘볼루션에서 시그마를 제외한 연산을 수행하는 것으로 보임

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] # output 노드 계산
print(output) # output 출력