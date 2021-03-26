import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
import numpy as np

xgboost = XGBRegressor(seed=0)

def train_model():

    con = sqlite3.connect('house_price.db')
    dataset = pd.read_sql_query('SELECT * FROM house_prices',con)
    print(dataset.head())

    X = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    X = pd.get_dummies(X)
    X  = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)

    xgboost.fit(X_train, y_train)
    y_pred = xgboost.predict(X_test)

    print('R2 value on test data:', r2_score(y_test,y_pred))


def predict(TotRmsAbvGrd, YearBuilt, LandContour, BsmtFinSF1, GarageCars, _1stFlrSF, TotalBsmtSF, _2ndFlrSF, GrLivArea, OverallQual):

    # LandContour is onehot encoded and the model was trained with the onehot columns last in order of all columns
    input = [TotRmsAbvGrd, YearBuilt, BsmtFinSF1, GarageCars, _1stFlrSF, TotalBsmtSF, _2ndFlrSF, GrLivArea, OverallQual, LandContour[0], LandContour[1], LandContour[2], LandContour[3]]
    price_prediction = xgboost.predict(np.reshape(np.array(input),(-1,13)))[0]

    return  price_prediction
