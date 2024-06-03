input_data=5
weight=3
target=8
learning_rate=0.1

pred=weight*input_data #예측 값 계산
error=pred-target #오차 계산
print("original error:", error)

slope=2*input_data*error #기울기 계산 및 가중치 조정
print("slope:",slope)

new_weight=weight-learning_rate*slope #가중치 변경
print("new weight:",new_weight)

new_pred=new_weight*input_data #새로운 예측값 계산
print("new prediction:", new_pred)

new_error=new_pred-target #새로운 오차
print("new error:", new_error)