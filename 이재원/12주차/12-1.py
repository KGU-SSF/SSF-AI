input_data =5 #입력값 5
weight =3 #가중치 3 
target = 8 # 실젯값 8
learning_rate = 0.01 # 러닝레이트(학습률) 0.01

pred = weight*input_data #예측값 = 가중치X입력값


error = pred - target #오차 = 예측값 - 실젯값 
print("original error:",error) 

slope = 2*input_data* error #기울기 = 2(입력값)X오차
print("slope:",slope)
new_weights = weight - learning_rate * slope #새로운 가중치 = 가중치 - (학습률X기울기)
print("new weight:",new_weights) 

new_pred = new_weights * input_data #새로운 예측값 = 새로운 가중치 X 입력값
print("new prediction:",new_pred)

new_error = new_pred - target #새로운 오차 = 새로운 예측값 - 실제값
print("new error:",new_error)
