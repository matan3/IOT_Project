from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn import preprocessing
import pandas as pd

url = "/home/gilad/Downloads/output2.csv"

# Assign colum names to the dataset
colnames = [ 'Class' , 'send', 'receive']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=colnames)

X = irisdata.drop('Class', axis=1)
y = irisdata['Class']

normalizer = preprocessing.Normalizer().fit(X)
X=normalizer.transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)



svclassifier = SVC(kernel='poly', degree=4,gamma='scale')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)


print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


svclassifier = SVC(kernel='rbf',gamma='scale') #or 'sigmoid' or 'rbf'
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))