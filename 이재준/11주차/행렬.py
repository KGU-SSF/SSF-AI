import numpy as np    #numpy 임포트
input_data = np.array([3, 5])

weight_hidden_0= np.array([2, 3])    #첫 은닉층 가중치
weight_hidden_1 = np.array([4, -5])   #두번 째 은닉층 가중치
weight_output = np.array([2, 7])      #세 번째 은닉층 가중치

hidden_0_value = (input_data * weight_hidden_0).sum() 
hidden_1_value = (input_data * weight_hidden_1).sum()   #은닉층 값계산
print(hidden_0_value, hidden_1_value, sep="")            #은닉층 값 출력
output = hidden_0_value* weight_output[0] + hidden_1_value* weight_output[1]   #출력층 값 계산
print(output)                                                             #출력층 값 출력

#실행결과는 21-13 -49 나왔습니다.
