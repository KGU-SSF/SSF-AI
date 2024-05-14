import numpy as np

Input_Data = np.array([3,5])
weight_hidden_0 = np.array([2,3])
weight_hidden_1 = np.array([4,-5])
weight_output = np.array([2,7])

hidden_value_0 = (Input_Data*weight_hidden_0).sum()
hidden_value_1 = (Input_Data*weight_hidden_1).sum()
print(hidden_value_0,hidden_value_1)

output = hidden_value_0 * weight_output[0] + hidden_value_1 * weight_output[1]
print(output)