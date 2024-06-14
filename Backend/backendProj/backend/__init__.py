from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

blacklist = set()
db=SQLAlchemy()
ma=Marshmallow()
cors = CORS()


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:adham12345@localhost/crypto_db2"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    db.init_app(app)
    ma.init_app(app)
    app.config['CORS_HEADERS']='Content-Type'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from backend.Views.views import views
    from backend.Auth.auth import auth
    from backend.Models.User import User
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    CORS(app,resources={'/*': {"origins": "*"}})
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


