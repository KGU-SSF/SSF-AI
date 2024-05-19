import numpy as np 

input_data = np.array([3,5]) #인풋 데이터로 1행으로 이루어진 [3,5]를 입력

weight_hidden_0=np.array([2,3]) #입력층에서 은닉층 1행 1열의 가중치 행렬이 [2,3]인 것을 뜻함
weight_hidden_1=np.array([4,-5]) #입력층에서 은닉층 1행 2열의 가중치 행렬이 [4,-5]인 것을 뜻함
weight_output=np.array([2,7]) #은닉층에서 결과층의 가중치 행렬이 [2,7]인 것을 뜻함

hidden_0_value=(input_data * weight_hidden_0).sum() #[3,5]에 2행 1열 크기의 [2,3]을 곱하여 은닉층 1행 1열은 [6+15]이므로 [21] 
hidden_1_value=(input_data * weight_hidden_1).sum() #[3,5]에 2행 1열 크기의 [4,-5]를 곱하여 은닉층 1행 2열은 [12-25]이므로 [-13]
print(hidden_0_value,hidden_1_value,sep=',') #은닉층 출력

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] #다시 [21, -13]에 2행 1열의 [2,7]을 곱하여 결과값은 [42-91]이므로 [-49]가 된다
print(output) 