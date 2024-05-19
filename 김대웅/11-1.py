import numpy as np

input_data = np.array([3,5]) #[3,5]를 정의한다.

weight_hidden_0 = np.array([2,3]) #weight_hidden_0을 정의한다.
weight_hidden_1 = np.array([4,-5]) #weight_hidden_1을 정의한다.
weight_output = np.array([2,7]) #weight_outpu을 정의한다.

hidden_0_value = (input_data * weight_hidden_0).sum() #hidden_0_value이 (3x2+5x3)=21이게 만들어준다
hidden_1_value = (input_data * weight_hidden_1).sum() #hidden_1_value이 {3x4+5x(-5)}=-13이게 만들어준다.
print(hidden_0_value, hidden_1_value, sep=',') #hidden_0_value과 hidden_1_value을 출력한다.

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #위에 hidden_0_value과 hidden_1_value의 값을 정의된 weight_output과 계산을한다.
print(output) #값을 출력한다.