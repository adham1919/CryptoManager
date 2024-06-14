




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import pandas as pd
import os



app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:adham12345@localhost/crypto_db2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
import datetime
