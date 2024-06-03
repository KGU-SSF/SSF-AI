import numpy as np
#input 값으로 3과 5 받기
input_data=np.array([3,5])

weight_hidden_0=np.array([2,3]) #weight_hidden_0 정의
weight_hidden_1=np.array([4,-5]) #weight_hidden_1 정의
weight_output=np.array([2,7])

hidden_0_value=(input_data*weight_hidden_0).sum() #3x2 + 5x3 = 21
hidden_1_value=(input_data*weight_hidden_1).sum() #3x4 + 5x(-5) = -13
print(hidden_0_value,hidden_1_value,sep=',') #hidden_0_value와 hidden_1_value 출력

output=hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1] #output 정의
print(output) #output 출력