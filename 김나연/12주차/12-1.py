#경사하강법
input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data
error = pred - target  #오차 
print("original error:", error)

slope = 2 * input_data * error   #오차함수의 기울기 
print("slope:", slope)

new_weight=weight-learning_rate*slope  #원래 있었던 가중치에서 learning rate 를 뺌 
print("new weight:", new_weight)  #새로운 가중치가 업데이트 됨 

new_pred=new_weight*input_data   #새로운 가중치를 사용하여 예측값 계산 
print("new predicition:", new_pred)

new_error=new_pred-target #새로운 오차 계산 
print("new error:", new_error)