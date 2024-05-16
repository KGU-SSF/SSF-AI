import numpy as np

input_data = np.array([3,5]) # 입력행렬 

weight_hidden_0 = np.array([2,3]) # 1번 노드에 가중치 전달 3 ->(2) = 6, 5 ->(3) = 15 // 6+15 = 21
weight_hidden_1 = np.array([4,-5]) # 2번 노드에 가줓치 전달 3 ->(4) = 12, 5 ->(-5) = -25 // 12 - 25 = -13
weight_output = np.array([2,7]) # 결과로 가는 가중치 전달방식 21 -> (2) = 42, -13 ->(7) = -91 // 42 -91 = -49

hidden_0_value = (input_data * weight_hidden_0).sum() #인공신경망의 원리가 행렬의 곱으로 표현할 수 있으므로 이롷게 표현
hidden_1_value = (input_data * weight_hidden_1).sum()
print(hidden_0_value, hidden_1_value, sep=',')

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]
print(output)