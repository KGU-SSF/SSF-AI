import numpy as np #넘파이 라이브러리를 가져옴

input_data = np.array([3, 5]) #입력 데이터를 인풋

weight_hidden_0 = np.array([2, 3]) 
weight_hidden_1 = np.array([4, -5])
weight_output = np.array([2, 7]) #각각 은닉층과 출력층의 가중치를 나타내는 넘파이 배열을 생성

hidden_0_value = (input_data * weight_hidden_0).sum()
hidden_1_value = (input_data * weight_hidden_1).sum() #각 은닉층의 입력과 가중치를 곱해서 합산
print(hidden_0_value, hidden_1_value, sep=',') #각 은닉층의 값을 출력

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #은닉층의 값에 해당하는 가중치를 곱한 후에 합산 (출력층의 값 계산)
print(output) #계산된 출력값을 프린트