import numpy as np

input_data = np.array([3,5]) #입력한 데이터를 인풋한다

weight_hidden_0 = np.array([2,3]) #출력층의 가중치를 나타내는 numpy 배열을 생성한다
weight_hidden_1 = np.array([4,-5]) #출력층의 가중치를 나타내는 numpy 배열을 생성한다
weight_output = np.array([2,7]) #출력층의 가중치를 나타내는 numpy 배열을 생성한다

hidden_0_value = (input_data * weight_hidden_0).sum() #입력과 가중치를 곱하여 합산한다
hidden_1_value = (input_data * weight_hidden_1).sum() #입력과 가중치를 곱하여 합산한다
print(hidden_0_value, hidden_1_value, sep=',') #값을 출력한다

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #은닉층의 값에 해당하는 가중치를 곱한 후에 합산한다
print(output) #계산된 출력값을 출력한다