input_data=5 
weight=3 #가중치
target=8 
learning_rate=0.1


pred= weight *input_data #예측값 =가중치x인풋데이터



error=pred-target
print("original error.",error)


slope = 2* input_data*error #슬로프=2차함수의기울기
print("slope.",slope)

new_weight=weight-learning_rate*slope
print("new weight:",new_weight)


new_pred=new_weight*input_data
print("new prediction:",new_pred)


new_error=new_pred-target
print("new error:",new_error)

