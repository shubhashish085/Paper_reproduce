from sklearn import cross_validation
import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

dataset = pd.read_csv('/home/antu/DataSet/DiscretizedData.csv')

#required_attributes = ['Age', 'Slope', 'Thalach', 'ResteCG', 'Thal', 'CP','Num']
#required_attributes = ['Slope', 'Age', 'CP', 'Thalach','Num']
required_attributes = ['CP', 'Oldpeak', 'Age', 'Slope', 'chol', 'Trestbps', 'Sex', 'Thalach','Num']

total_array = numpy.zeros(shape=(len(dataset),len(required_attributes)-1))
labels = numpy.zeros(shape=(len(dataset)))

for i in range (len(dataset)):
    for j in range(len(required_attributes) - 1):
        total_array[i][j] = dataset[required_attributes[j]][i]

    labels[i] = dataset[required_attributes[8]][i]


clf = SVC()

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(total_array,labels, test_size=0.2)

clf.fit(features_train,labels_train)

predicted_array = clf.predict(features_test)

accuracy = accuracy_score(labels_test,predicted_array)

print(accuracy)







