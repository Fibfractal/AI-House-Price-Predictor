import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

xgboost = XGBRegressor(seed=0)

def train_model():

    con = sqlite3.connect('house_price.db')
    dataset = pd.read_sql_query('SELECT * FROM house_prices',con)
    print(dataset.head())

    X = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    X = pd.get_dummies(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)

    xgboost.fit(X_train, y_train)
    y_pred = xgboost.predict(X_test)

    print('R2 value on test data:', r2_score(y_test,y_pred))