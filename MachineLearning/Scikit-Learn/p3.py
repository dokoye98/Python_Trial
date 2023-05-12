import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model,datasets


iris = datasets.load_iris()

x = iris.data[:,:2]
y = iris.target

lm = linear_model.LogisticRegression(C=1e5)

lm.fit(x,y)
x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5

y_min, y_max = y[:,1].min() - .5, y[:,1].max() + .5

h= .02

