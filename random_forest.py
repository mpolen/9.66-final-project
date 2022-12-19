import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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

    knn_model = RandomForestClassifier()
    knn_model.fit(X_train, y_train)

    return knn_model

def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    y_prob = clf_object.predict_proba(X_test)
    print("Predicted probabilities:")
    print(np.array(['always_4', 'bias_4', 'fair', 'only_2_or_3']))
    print(y_prob)
    return y_pred, y_prob
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : \n",
    classification_report(y_test, y_pred))


def main():
   
    # Building Phase
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    knn = createAndTrainModel(X_train, y_train)
      
    # Operational Phase      
      
    print("Results Using KNN on Test Data:")
    # Prediction using knn
    y_pred = prediction(X_test, knn)[0]
    cal_accuracy(y_test, y_pred)

    X_test = np.array([[1, 3, 4, 4, 1, 3, 2, 3],
                        [4, 4, 4, 4, 4, 4, 4, 2],
                        [4, 4, 4, 4, 4, 4, 4, 4],
                        [3, 3, 3, 3, 2, 2, 2, 3]])

    y_test = np.array(['fair', 'bias_4', 'always_4', 'only_2_or_3'])
    print("Results Using KNN on 4 sequences:")
    # # Prediction using knn
    y_pred = prediction(X_test, knn)[0]
    cal_accuracy(y_test, y_pred)


# Calling main function
if __name__=="__main__":
    main()