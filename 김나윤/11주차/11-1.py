# numpy 라이브러리
import numpy as np

# 입력층 넘파이 배열
input_data = np.array([3, 5])

# 가중치 넘파이 배열
weight_hidden_0 = np.array([2, 3])
weight_hidden_1 = np.array([4, -5])
weight_output = np.array([2, 7])

# 입력층 * 가중치 = 은닉층 값
hidden_0_value = (input_data * weight_hidden_0).sum()
hidden_1_value = (input_data * weight_hidden_1).sum()
print(hidden_0_value, hidden_1_value, sep=',')

# ∑ (은닉층 값 * 가중치) = 출력층(예측값)
output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]
print(output)

"""
실제값 - 예측값 = 오차
오차를 최대한 줄이는 것이 목표
"""