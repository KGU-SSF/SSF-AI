from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
diabetes = load_diabetes()
X_data = diabetes.data
y_data = diabetes.target
x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)
LinearRegression()
y_train_pred = lr.predict(x_train)
r2_train = r2_score(y_train, y_train_pred)
print(f"r2_train: {r2_train}")
y_test_pred = lr.predict(x_test)
r2_test = r2_score(y_test, y_test_pred)
print(f"r2_test: {r2_test}")