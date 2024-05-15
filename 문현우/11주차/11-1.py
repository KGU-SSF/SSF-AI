import numpy as np #numpy를 np라는 이름으로 가져옴
#이 구조는 다층 퍼셉트론 인공 신경망을 구현 한것임

##다층 퍼셉트론 설명((https://youtu.be/mlsCX5sL76E?si=iYbtxU7iWVy27DUZ))

input_data=np.array([3,5]) #입력층 대입
## 쉽게 기호로 표현하겠음
weight_hidden_0=np.array([2,3]) #은닉층 사이의 가중치  (1)
weight_hidden_1=np.array([4,-5])#은닉층 사이의 가중치  (2)
weight_output=np.array([2,7]) #출력층 사이의 가중치    (**)

hidden_0_value=(input_data*weight_hidden_0).sum() #은닉층 결과값(a): 입력층의 값과 (1)의 값을 내적
hidden_1_value=(input_data*weight_hidden_1).sum() #은닉층 결과값(b): 입력층의 값과 (2)의 값을 내적
print(hidden_0_value,hidden_1_value,sep=',') #은닉층의 결과값을 보여줌
output=hidden_0_value*weight_output[0]+hidden_1_value*weight_output[1] #출력값=은닉층의 값과 (**)내적의 값
print(output)


