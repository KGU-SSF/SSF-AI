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

y_train_pred = lr.predict(x_train)
r2_train = r2_score(y_train, y_train_pred)
print(f"r2_train: {r2_train}")
y_test_pred = lr.predict(x_test)
r2_test = r2_score(y_test, y_test_pred)
print(f"r2_test: {r2_test}")

weight = np.random.rand(x_train.shape[1])
bias = 0
learning_rate = 0.001

def predict(X, W, b):
  return X.dot(W) + b

def gradient(X, error):
  return 2 * X.T.dot(error), np.sum(error)

def update(W, b, gd, learning_rate):
  W = W - learning_rate * gd[0]
  b = b - learning_rate * gd[1]
  return W, b

def cost(error):
  return (error**2).mean()


epoch = 1000
for i in range(epoch):
  pred = predict(x_train, weight, bias)
  error = pred - y_train
  print(f"cost at epoch {i+1}: {cost(error):.4f}")
  gd = gradient(x_train, error)
  weight, bias = update(weight, bias, gd, learning_rate)
y_train_pred = predict(x_train, weight, bias)
r2_train = r2_score(y_train, y_train_pred)
print(f"r2_train: {r2_train}")
y_test_pred = predict(x_test, weight, bias)
r2_test = r2_score(y_test, y_test_pred)
print(f"r2_test: {r2_test}")