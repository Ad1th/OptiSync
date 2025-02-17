from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBRegressor
import pandas as pd
import numpy as np
RANDOM_STATE=55
df=pd.read_csv("/Users/amangolani/Downloads/Final Data/Reduced_Cost_Data.csv")
df["Datetime"] = pd.to_datetime(df["Datetime"], errors='coerce')
df = df.dropna()  # Drop rows where datetime conversion failed
df = df.sort_values("Datetime")

    # Convert 'Datetime' to Unix timestamp
df["Timestamp"] = df["Datetime"].astype('int64')
df = pd.get_dummies(df, columns=["Mill_Size", "Location"], drop_first=True)

X=df.drop(columns=['Datetime', 'Current_Bill_Amount'])
y=df['Current_Bill_Amount']


scaler_y = MinMaxScaler()
y = scaler_y.fit_transform(y.values.reshape(-1, 1))  # Standardize target variable
scaler_x = MinMaxScaler()
X=scaler_x.fit_transform(X)
#predict the cost of the inputted stuff and what we could ge it down to and also what is the energy consumption we can get to 
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=RANDOM_STATE)
#random_forest_algo=RandomForestRegressor(n_estimators=100,max_depth=20,min_samples_split=10).fit(X_train,y_train)
#random_forest_algo=XGBRegressor(n_estimators=250,learning_rate=0.06,verbosity=1,random_state=RANDOM_STATE).fit(X_train,y_train)
random_forest_algo = XGBRegressor(
    n_estimators=180,
    learning_rate=0.05,
    max_depth=3,
    min_child_weight=7,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.5,
    reg_lambda=1,
    verbosity=1,
    random_state=RANDOM_STATE
).fit(X_train, y_train)

train_mse = mean_squared_error(y_train, random_forest_algo.predict(X_train))
test_mse = mean_squared_error(y_test, random_forest_algo.predict(X_test))

print(f"Metrics train:\n\tMSE: {train_mse:.4f}")
print(f"Metrics test:\n\tMSE: {test_mse:.4f}")