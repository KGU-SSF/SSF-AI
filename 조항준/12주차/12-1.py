input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data                     #예측값 = 가중치 * 입력값
error = pred - target                           #오차 = 예측값 - 실제값
print("original error:", error)                    

slope = 2 * input_data * error                #오차함수의 기울기 = 2 * 입력값 * 오차
print("slope:",slope)                       

new_weight = weight - learning_rate * slope      #새로운 가중치 = 가중치 - 러닝레이트 * 오차함수 기울기
print("new weight:", new_weight)                   

new_pred = new_weight * input_data                   #새로운 예측값 = 새로운 가중치 * input_data
print("new prediciton:", new_pred)                 

new_error = new_pred - target                            #새로운 오차 = 새로운 예측값 - 실제값
print("new error:", new_error)

#original error : 오차 (7)
#slope : 오차함수의 기울기 (70)
#new_weight : 새로운 가중치 (-4.0)
#new_prediction : 새로운 예측값 (-20.0)
#new_error : 새로운 오차 (-28.0)

