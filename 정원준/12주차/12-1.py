input_data=5
weight=3    #가중치
target=8    #실제값
learning_rate=0.1

pred=weight*input_data  #예측값=가중치*입력값
error=pred - target     #오차=예측값-실제값
print("original error:", error)

slope=2*input_data*error    #오차함수의 기울기=2*입력값*오차
print("slope:", slope)

new_weight=weight-learning_rate*slope   #새로운 가중치로 업데이트
print("new weight:", new_weight)

new_pred=new_weight*input_data  #새로운 예측값=새로운 가중치*입력값
print("new prediction:", new_pred)

new_error=new_pred-target   #새로운 오차=새로운 예측값-실제값
print("new error:", new_error)