import numpy as np

input_data = np.array([3,5])    #입력값[3,5] 정의하기

weight_hidden_0 = np.array([2,3])   #첫번째 입력값의 가중치[2,3]정의
weight_hidden_1 = np.array([4,-5])  #두번째 입력값의 가중치[4,-5]정의
weight_output = np.array([2,7])     #weight_hidden_0의 가중치 2와 weight_hidden_1의 가중치 7을 정의 

hidden_0_value = (input_data*weight_hidden_0).sum() #hidden_0_value을 계산하여 3x2+5x3=21으로 정의
hidden_1_value = (input_data*weight_hidden_1).sum() #hidden_1_value을 계산하여 3x4+5x(-5)=-13으로 정의
print(hidden_0_value, hidden_1_value, sep=',')  #hidden_0_value와hidden_1_value인 21,-13출력

output = hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1]    #hidden_0_value와 hidden_1_value을 weight_output에서 정의된 2와 7을 각각 곱한후 더함
print(output)   #21x2+(-13)x7=-49출력