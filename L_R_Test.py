"""First ML Test."""

from pandas import read_csv
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# load dataset
urls = ["data_files\January-March_even_split.csv"]
for url in urls:
    names = ['Total Transactions', 'Account Status']
    dataset = read_csv(url, names=names)

    # Split-out validation dataset
    array = dataset.values
    X = array[:, 0:1]
    y = array[:, 1]
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

    # Make predictions on validation dataset
    # model = SVC()
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)

    # Evaluate predictions
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions, digits=7))
    
    fig = plt.figure(figsize=(10,5))
    xlabel = 'Total Transactions'
    ylabel = 'Account Status'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(X_validation, Y_validation, color='red')
    plt.show()

# for i in range(len(X_validation)):
#     print("X=%s, Predicted=%s" % (X_validation[i], predictions[i]))
