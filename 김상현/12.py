input_date = 5
weight = 3
target = 8
learning_rate = 0.1
pred = weight*input_date

error = pred - target
print("original error", error)

slope = 2*input_date*error
print("slope",slope)

new_weight = weight-learning_rate*slope
print("new weight", new_weight)

new_pred = new_weight*input_date
print("new predicition",new_pred)

new_error = new_pred - target
print("new error", new_error)
