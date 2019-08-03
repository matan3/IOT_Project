from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn import svm
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


url = "C:\\Users\\Matan\\Downloads\\output.csv"

# Assign colum names to the dataset
colnames = ['Class', 'send', 'receive']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=colnames)

# show before SVM
sns.lmplot('send','receive',data=irisdata,hue='Class',
           palette='Set1', fit_reg=False, scatter_kws={"s":70})
plt.show()

colnames.remove('Class')
X = irisdata[colnames].values
y = irisdata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#The Design of hyperplane
# Get the separating hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30, 10000)
yy = a * xx - (model.intercept_[0]) / w[1]

# Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

sns.lmplot('send','receive',data=irisdata,hue='Class',
           palette='Set1', fit_reg=False, scatter_kws={"s":70})
plt.plot(xx, yy, linewidth=2, color='black');
plt.show()

sns.lmplot('send','receive',data=irisdata,hue='Class',
           palette='Set1', fit_reg=False, scatter_kws={"s":70})
plt.plot(xx, yy, linewidth=2, color='black')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
            s=80, facecolors='none');
plt.show()

