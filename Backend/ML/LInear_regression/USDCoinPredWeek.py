import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math
import matplotlib.pyplot as mp
from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sb
  


Doge = pd.read_csv("coin_USDCoin.csv")
#Pearson  correlation feature selection model
Doge.corr()
  

projection_Doge = 7
#creation of a new column with a name prediction
Doge['Prediction'] =   Doge[['Close']].shift(-projection_Doge)

X_Doge = np.array( Doge[['Close']])
X_Doge = X_Doge[:-projection_Doge]
y_Doge =   Doge['Prediction'].values
y_Doge = y_Doge[:-projection_Doge]
x_train_Doge, x_test_Doge, y_train_Doge, y_test_Doge = train_test_split(X_Doge,y_Doge,test_size=0.3)
linReg_Doge = LinearRegression()
linReg_Doge.fit(x_train_Doge,y_train_Doge)
x_projection_Doge = np.array(Doge[['Close']])[-projection_Doge:]
linReg_prediction_Doge = linReg_Doge.predict(x_projection_Doge)
print(linReg_prediction_Doge)