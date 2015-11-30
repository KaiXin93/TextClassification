# encoding=utf-8
__author__ = 'qkx'
from svmutil import *

y, x = svm_read_problem("../heart_scale")
print(y)
print(x)
m = svm_train(y[:200], x[:200], "-c 4")
p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)

print("-------------------------------")

y, x = [1, -1], [[1, 0, 1], [-1, 0, -1]]
# Sparse data
y, x = [1, -1], [{1: 1, 3: 1}, {1: -1, 3: -1}]
print(y)
print(x)
prob = svm_problem(y, x)
param = svm_parameter('-c 4 -b 1')
m = svm_train(prob, param)


words = u'我'
print(type(words))
print(type(words.encode("gbk")))

