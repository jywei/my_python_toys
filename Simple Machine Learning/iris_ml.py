# Machine Learning: Iris

from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print(iris.data.shape)

model = svm.LinearSVC()  # chose model
model.fit(iris.data, iris.target)  # train model
model.predict([[5.0, 4.0, 2.0, 0.5]])  #predict the type of iris of [5.0, 4.0, 2.0, 0.5]
