import numpy as np

input_data = np.array([3,5]) # �ʱ� array �Է�

weight_hidden_0 = np.array([2,3]) # 0�� hidden ����� ����ġ
weight_hidden_1 = np.array([4,-5]) # 1�� hidden ����� ����ġ
weight_output = np.array([2,7]) # output ��� ����ġ

hidden_0_value = (input_data * weight_hidden_0).sum() # hidden_0 ��� ���
hidden_1_value = (input_data * weight_hidden_1).sum() # hidden_1 ��� ���
print(hidden_0_value, hidden_1_value, sep=",") # hidden layer�� ��� �� ���

# ������ �˴� ��İ��� �ƴ� ����, �ܺ���ǿ��� �ñ׸��� ������ ������ �����ϴ� ������ ����

output = hidden_0_value * weight_output[0] + hidden_1_value * weight_output[1] # output ��� ���
print(output) # output ���