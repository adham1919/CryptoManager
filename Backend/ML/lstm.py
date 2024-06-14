from math import sqrt

import keras.models
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

import numpy as np
import seaborn as sns
import joblib


model = keras.models.load_model('my_model1')



data=pd.read_csv("mydata7.csv")
datag=data[['Price','Sentiment']].groupby(data['Time']).mean()
from sklearn.preprocessing import MinMaxScaler

values=datag['Price'].values.reshape(-1,1)
sentiment=datag['Sentiment'].values.reshape(-1,1)

scaler=MinMaxScaler(feature_range=(0,1))
scaled=scaler.fit_transform(values)
train_size=int(len(scaled)*0.7)
test_size=len(scaled) - train_size
train,test=scaled[0:train_size,:],scaled[train_size:len(scaled),:]
print(len(train),len(test))
split=train_size
print(test)



def create_dataset(dataset,look_back,sentiment,sent=False):
    dataX,dataY=[],[]
    for i in range(len(dataset) - look_back):
        if i >= look_back:
            a=dataset[i - look_back:i + 1,0]
            a=a.tolist()
            if (sent == True):
                a.append(sentiment[i].tolist()[0])
            dataX.append(a)
            dataY.append(dataset[i + look_back,0])
    # print(len(dataY))
    return np.array(dataX),np.array(dataY)


look_back=1
trainX,trainY=create_dataset(train,look_back,sentiment[0:train_size])
testX,testY=create_dataset(test,look_back,sentiment[train_size:len(scaled)])
trainX=np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX=np.reshape(testX,(testX.shape[0],1,testX.shape[1]))

yhat=model.predict(testX)
yhat_inverse_1=scaler.inverse_transform(yhat.reshape(-1,1))
xhat_inverse_1=scaler.inverse_transform(testX.reshape(-1,1))
testY_inverse_1=scaler.inverse_transform(testY.reshape(-1,1))
print(testX)
pyplot.plot(yhat_inverse_1,label='predict')
pyplot.plot(testY_inverse_1,label='true')


pyplot.show()

print("))))))))))))))))))))))))")
print(xhat_inverse_1)
print("))))))))))))))))))))))))")
print(yhat_inverse_1)
print(testY_inverse_1)
rmse_1=sqrt(mean_squared_error(testY_inverse_1,yhat_inverse_1))
print('Test RMSE: %.3f'%rmse_1)

"""
model = keras.models.load_model('my_model2')


look_back=2
trainX,trainY=create_dataset(train,look_back,sentiment[0:train_size])
testX,testY=create_dataset(test,look_back,sentiment[train_size:len(scaled)])

trainX=np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX=np.reshape(testX,(testX.shape[0],1,testX.shape[1]))
yhat=model.predict(testX)
pyplot.plot(yhat,label='predict')
pyplot.plot(testY,label='true')
pyplot.legend()
pyplot.show()

yhat_inverse_2=scaler.inverse_transform(yhat.reshape(-1,1))
testY_inverse_2=scaler.inverse_transform(testY.reshape(-1,1))

rmse_2=sqrt(mean_squared_error(testY_inverse_2,yhat_inverse_2))
print('Test RMSE: %.3f'%rmse_2)

model = keras.models.load_model('my_model3')

look_back=3
trainX,trainY=create_dataset(train,look_back,sentiment[0:train_size])
testX,testY=create_dataset(test,look_back,sentiment[train_size:len(scaled)])

trainX=np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX=np.reshape(testX,(testX.shape[0],1,testX.shape[1]))


yhat=model.predict(testX)
pyplot.plot(yhat,label='predict')
pyplot.plot(testY,label='true')
pyplot.legend()
pyplot.show()

yhat_inverse_3=scaler.inverse_transform(yhat.reshape(-1,1))
testY_inverse_3=scaler.inverse_transform(testY.reshape(-1,1))
rmse_3=sqrt(mean_squared_error(testY_inverse_3,yhat_inverse_3))
print('Test RMSE: %.3f'%rmse_3)





model = keras.models.load_model('my_model4')


look_back=2
trainX,trainY=create_dataset(train,look_back,sentiment[0:train_size],sent=True)
testX,testY=create_dataset(test,look_back,sentiment[train_size:len(scaled)],sent=True)

trainX=np.reshape(trainX,(trainX.shape[0],1,trainX.shape[1]))
testX=np.reshape(testX,(testX.shape[0],1,testX.shape[1]))


yhat=model.predict(testX)
pyplot.plot(yhat,label='predict')
pyplot.plot(testY,label='true')
pyplot.legend()
pyplot.show()

yhat_inverse_sent=scaler.inverse_transform(yhat.reshape(-1,1))
testY_inverse_sent=scaler.inverse_transform(testY.reshape(-1,1))

rmse_sent=sqrt(mean_squared_error(testY_inverse_sent,yhat_inverse_sent))
print('Test RMSE: %.3f'%rmse_sent)

"""