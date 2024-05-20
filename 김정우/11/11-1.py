import numpy as np

input_data = np.array([3,5]) #입력값 [3,5]생성

weight_hidden_0 = np.array([2,3]) #입력값에 대한 가중치 [2.3]생성
weight_hidden_1 = np.array([4,-5]) #입력값에 대한 두번째 가중치 [4,-5]생성
weight_output = np.array([2,7]) #weight_hidden_0에대한 가중치 2와 weight_hidden_1에대한 가중치 7 [2,7]생성

hidden_0_value = (input_data * weight_hidden_0).sum() #입력값에 가중치를 곱한 값 3*2+5*3=21
hidden_1_value = (input_data * weight_hidden_1).sum() #입력값에 두번째 가중치를 곱한 값 3*4+5*(-5)=-13
print(hidden_0_value,hidden_1_value,sep=',') #21,-13 출력

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #21*2+(-13)*7=-49 의 결과인 -49를 output에 넣음

print(output) #-49 출력
