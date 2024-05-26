input_data=5 # 입력값
weight=3 # 가중치
target=8 # 실제값
learning_rate=0.1 # 학습률

pred = weight * input_data # 예측값은 가중치 * 입력값
 
error = pred-target # 오차는 예측값 - 실제값 
print("original error", error) # 오차 = 7 

slope=2*input_data*error # 오차함수의 기울기는 2 * 입력값 * 오차
print("slope", slope) # 기울기 = 70

new_weight=weight-learning_rate*slope # 새로운 가중치를 업데이트함 (기존 가중치 - 학습률 * 기울기)
print("new weight", new_weight) # 새로운 가중치 -4.0

new_pred=new_weight*input_data # 새로운 예측값은 새로운 가중치 * 입력값
print("new prediction:", new_pred) # 새로운 예측값 -20.0

new_error=new_pred-target # 새로운 오차는 새로운 예측값 - 실제값 
print("new error", new_error) # 새로운 오차 -28.0