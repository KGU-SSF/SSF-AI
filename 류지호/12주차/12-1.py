input_data=5 #입력값
weight=3    #가중치
target=8    #실제값
learning_rate=0.1  #학습비율

pred=weight*input_data #예측값
 
error=pred-target    #오차
print("original error:", error)

slope=2*input_data*error  #기울기 y=2x (x=error)   
print("slope:", slope)

new_weight=weight-learning_rate*slope   #새 가중치
print("new weight:", new_weight)

new_pred=new_weight*input_data       #새 예측값
print("new prediction:", new_pred)

new_error=new_pred-target    #새 오차
print("new error:", new_error)