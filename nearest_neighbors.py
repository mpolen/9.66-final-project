import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report




def importdata():
    balance_data = pd.read_csv('data.data')
      
    # Printing the dataswet shape
    print ("Dataset Length: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)
      
    # Printing the dataset obseravtions
    print ("Dataset: ",balance_data.head())
    return balance_data
  
# Function to split the dataset
def splitdataset(balance_data):
  
    # Separating the target variable
    X = balance_data.values[:, 1:9]
    Y = balance_data.values[:, 0]
  
    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)
      
    return X, Y, X_train, X_test, y_train, y_test


def createAndTrainModel(X_train, y_train):

    knn_model = KNeighborsClassifier(n_neighbors=3)
    knn_model.fit(X_train, y_train)

    return knn_model

def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))


def main():
    X_test = np.array([[ 4, 4, 4, 4, 4, 4, 4, 2],
                        [4, 4, 4, 4, 4, 4, 4, 4],
                        [1, 3, 4, 4, 1, 3, 2, 3],
                        [3, 3, 3, 3, 2, 2, 2, 3]])

    y_test = np.array(['bias_4', 'always_4', 'fair', 'only_2_or_3'])
    # Building Phase
    data = importdata()
    X, Y, X_train, _, y_train, _ = splitdataset(data)
    knn = createAndTrainModel(X_train, y_train)
      
    # Operational Phase      
      
    # print("Results Using KNN:")
    # # Prediction using knn
    y_pred = prediction(X_test, knn)
    cal_accuracy(y_test, y_pred)


# Calling main function
if __name__=="__main__":
    main()