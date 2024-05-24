import numpy as np

input_data=np.array([3,5])                 #행렬(2,1)을 만들고 거기에 각각 3 과 5를 넣음

weight_hidden_0=np.array([2,3])             #행렬(1,2)을 만들고 각각 2와 3 해당하게 함
weight_hidden_1=np.array([4,-5])             #행렬(1,2)을 만들고 각각 4와 -5 해당하게 함
weight_output=np.array([2,7])                #행렬(1,2)을 만들고 각각 2와 7 해당하게 함

hidden_0_value=(input_data*weight_hidden_0).sum()              #3과 가중치 2 / 5와 가중치 3을 곱하고 각각 더해줌
hidden_1_value=(input_data*weight_hidden_1).sum()              #3과 가중치 4/  5와 가중치 -5를 곱하고 각각 더해줌
print(hidden_0_value,hidden_1_value,sep=",")                         #가중치를 적용한 값 각각 출력

output=hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1]        #가중치를 적용한 값[0]과 2 / 가중치를 적용한 값[1]과 7을 곱해서 각각 더해줌
print(output)                                                               # 위의 값 출력