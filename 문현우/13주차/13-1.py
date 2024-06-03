from sklearn.datasets import load_diabetes#당뇨병 데이터 세트를 로드하기위해
from sklearn.model_selection import train_test_split #데이터를 학습세트와 테스트 세트로 나누기 위해
from sklearn.linear_model import LinearRegression #선형회귀 모델을 구현하기 위해
from sklearn.metrics import r2_score #모델 성능 평가위해 
import numpy as np

diabetes=load_diabetes() #당뇨병 데이터세트 로드
x_data=diabetes.data #입력 특성 데이터
y_data=diabetes.target #타겟값(당뇨병 진행정도)

x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2, random_state=42)
#학습 세트와 테스트 세트로 나눔
#test_size=0.2=>전체 데이터의 20%를 테스트세트에 사용
#random_state=42는 데이터 분할 시 일관성을 위해 사용되는 시드 값.

lr=LinearRegression()#LinearRegression객체생성
lr.fit(x_train,y_train)
#fit메서드 사용하여 선형회귀모델 학습시킴

y_train_pred=lr.predict(x_train)#학습 세트에 대해 예측값을 생성
r2_train=r2_score(y_train,y_train_pred)
print(f"r2_train: {r2_train}")
y_test_pred=lr.predict(x_test)
r2_test=r2_score(y_test,y_test_pred)
print(f"r2_test:{r2_test}")
