import numpy as np

input_data = np.array([3,5]) #input data

weight_hidden_0 = np.array([2,3]) #첫번째 input data에 대한 weight
weight_hidden_1 = np.array([4,-5]) #두번째 input data에 대한 weight
weight_output = np.array([2,7]) #weight_hidden_0, 1에 대한 weight

hidden_0_value = (input_data * weight_hidden_0).sum() #cal: 3*2 + 5*3 = 21
hidden_1_value = (input_data * weight_hidden_1).sum() #cal: 3*4 - 5*5 = -13
print(hidden_0_value, hidden_1_value, sep=',')

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #cal: 21*2 - 13*7 = -49

print(output)