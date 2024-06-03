input_data=5 #값
weight=3    #가중치
target=8    #목표값
learning_rate=0.1 #런닝레이트
pred=weight*input_data #예측값=가중치*데이타
error=target-pred #오류값=원래 목표값-예측값
print("original error",error)
slope=2*error*input_data #오류함수 기울기=2*오류*데이터값
'''오류 함수가 y=x^2이므로 미분하면 y'=2*x이지만 *input_data도 곱해줘야한다
#왜 input_data도 곱해야 하는가?
# => f=(weight*input_data)−target 즉 오류
# 오류 함수는 E=f^2=((weight*input_data)-target)^2
위에 처럼 나오는데 이를 weight에 대해 미분을하면
E'=2f*f'(f'=f를 weigth에 대해 미분)
E'=2*((weight*input_data)-target)*(input_data)  {f'미분하면 target이 상수취급이므로 input_data만남음 }
즉 slope=2*error*input_datan '''
print("slope",slope)

#그럼 이제 새로운 가중치를 구해줘야함
new_weight=weight-learning_rate*slope
#새로운 가중치=원래 가중치-러닝레이트*오류함수의 기울기
print("new weight",new_weight)

new_pred=new_weight*input_data#새로운 예측
print("new prediction",new_pred)

new_error=new_pred-target  #새로운 오차값
print("new error",new_error)


