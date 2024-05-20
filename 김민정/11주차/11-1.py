import numpy as np

input_data=np.array([3,5]) #입력 데이터 정의

weight_hidden_0=np.array([2,3]) #입력값에 의한 가중치 
weight_hidden_1=np.array([4,-5]) #두번째 입력값에 대한 가중치 
weight_output=np.array([2,7]) #2는 weight_hidden_0의 가중치 7은 weight_hidden_1의 가중치

hidden_0_value=(input_data*weight_hidden_0).sum() #계산:'(3*2)+(5*3)=6+15=21'
hidden_1_value=(input_data*weight_hidden_1).sum() #계산:'(3*4)+(5*-5)=12+(-25)=-13
print(hidden_0_value,hidden_1_value,sep=',') # 두 계산값을 출력, 출력:'21,-13'


output=hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1] # 각 value 값에 해당 가중치를 곱하고 합산하여 계산, 계산:'(21*2)+(-13*7)=42+(-91)=-49
print(output) #최종 출력 값을 출력, 출력:'-49'