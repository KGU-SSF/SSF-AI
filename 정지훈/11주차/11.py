import numpy as np

input_data = np.array([3, 5]) # 입력 값을 정의하는 부분


weight_hidden_0 = np.array([2, 3]) #입력 값의 가중치 [2,3]
weight_hidden_1 = np.array([4, -5]) #두 번째 입력값에 대한 가중치 [4,5]

# 출력층 뉴런의 가중치를 정의
weight_output = np.array([2, 7])

# input_data와 weight_hidden_0의 원소별 곱셈 결과는 [3*2, 5*3] = [6, 15]
# hidden_0_value = 6 + 15 = 21
hidden_0_value = (input_data * weight_hidden_0).sum()

# input_data와 weight_hidden_1의 원소별 곱셈 결과는 [3*4, 5*(-5)] = [12, -25]
# hidden_1_value = 12 - 25 = -13
hidden_1_value = (input_data * weight_hidden_1).sum()

# 은닉층 뉴런들의 값을 출력 (콤마로 구분)
print(hidden_0_value, hidden_1_value, sep=',')

# hidden_0_value와 weight_output[0]의 곱은 21 * 2 = 42
# hidden_1_value와 weight_output[1]의 곱은 -13 * 7 = -91
# 출력 값은 42 + (-91) = -49
output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]

print(output)
