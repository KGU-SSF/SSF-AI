import numpy as np                                                                  #numpy 라이브러리 추가

input_data = np.array([3,5])                                                        #입력값 3, 5를 가짐

weight_hidden_0 = np.array([2,3])                                                   #첫번째 뉴런과 연결된 은닉층의 가중치는 2, 3이다
weight_hidden_1 = np.array([4,-5])                                                  #두번째 뉴련과 연결된 은닉층의 가중치는 4, -5이다
weight_output = np.array([2,7])                                                     #출력층의 뉴런과 연결된 가중치는 2, 7이다

hidden_0_value = (input_data * weight_hidden_0).sum()                               #hidden_0_value = ( 3*2 ) + ( 5*3 ) = 21
hidden_1_value = (input_data * weight_hidden_1).sum()                               #hidden_1_value = ( 3*4 ) + ( 5*(-5) ) = -13
print(hidden_0_value, hidden_1_value, sep = ",")                                    #두 값을 콤마로 구분하여 출력한다

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1]      #( 21*2 ) + ( -13*7 ) = -49
print(output)                                                                       #-49 출력