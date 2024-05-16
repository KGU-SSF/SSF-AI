import numpy as np

input_data=np.array([3,5]) #입력이라는 새로운 데이터가 들어감 3과 5가 먼저 들어감 3에서 화살표가 2개, 5에서도 화살표가 2개

weight_hidden_0=np.array([2,3]) #3에서 2만큼 곱하고 다음으로 넘겨줌 5에서 3만큼 곱하고 다음으로 넘겨줌 
weight_hidden_1=np.array([4,-5]) #3에서 4만큼 곱하고 다음으로 넘겨줌 5에서 -5만큼 곱하고 다음으로 넘겨줌
#두번에 하면 더 정확한 값을 가짐 weight는 가중치를 뜻함
weight_output=np.array([2,7]) #출력에 대한 가중치 
#(1, 1)인 [21]와 (1, 1)인 [2]를 곱해서 42, (1, 1)인 [-13]와 (1, 1)인 [7]를 곱해서 -91 을 더한 42+-91=-49로 -49가 나옴

hidden_0_value=(input_data*weight_hidden_0).sum()
hidden_1_value=(input_data*weight_hidden_1).sum()
print(hidden_0_value, hidden_1_value, sep=',')

output=hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1]
print(output)