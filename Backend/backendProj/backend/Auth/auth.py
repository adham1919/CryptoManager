import json
import uuid

from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify,current_app as app
from backend.Models.User import User
from werkzeug.security import generate_password_hash,check_password_hash
from backend import db
import jwt
import datetime
from backend.Annots.annotations import token_required
from backend import blacklist
from backend.Models.Wallet import WalletSchema
from backend.Models.Watchlist import WatchlistSchema

auth=Blueprint('auth',__name__)


@auth.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    user_name=data['user_name']
    password=data['password']
    user=User.query.filter_by(user_name=user_name).first()
    if user:
            if check_password_hash(user.password,password):
               # flash('Logged in successfully!',category='success')
               token=jwt.encode( {'public_id': user.public_id,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},app.config['SECRET_KEY'])
               return jsonify({"status":200,'message': 'Logged in successfully','token': token})
            else:
                #flash('Incorrect password, try again.',category='error')
                return jsonify({'status':401,'message': 'Incorrect password.'})
    else:
        # flash('Email does not exist.',category='error')
         return jsonify({'status':401,'message': 'Username does not exist.'})

    return  jsonify({'status':500,'message': 'Sql error'})


@auth.route('/logout' ,methods=['POST'])
@token_required
def logout(current_user):
    token=None
    print("CALLED LOGOUT")
    if 'x-access-token' in request.headers:
        token=request.headers['x-access-token']
    blacklist.add(token)
    return jsonify({'message': 'Logget out successfully'})

@auth.route('/try',methods=['POST'])
@token_required
def tryit(current_user):
    return jsonify({'message': 'you are Logged in '})


@auth.route('/user',methods=['GET'])
@token_required
def getUser(current_user):
    email=current_user.email
    user_name=current_user.user_name
    budget=current_user.budget
    wallet=current_user.wallet
    watchlist=current_user.watchlist
    watchlist_schema=WatchlistSchema(many=True)
    watch_res=watchlist_schema.dump(watchlist)
    wallet_schema=WalletSchema(many=True)
    wallet_res=wallet_schema.dump(wallet)
    newsletter=current_user.newsletter
    print(wallet_res)
    print(watch_res)
    return jsonify({'user_name': user_name ,'email': email , 'budget': budget,'wallet' : wallet_res,'watchlist': watch_res,'newsletter': newsletter})


@auth.route('/signup',methods=['POST'])
def sign_up():
    data=request.get_json()
    email=data['email']
    user_name=data['user_name']
    password1=data['password1']
    password2=data['password2']

    user=User.query.filter_by(email=email).first()
    user2=User.query.filter_by(user_name=user_name).first()
    if user:
       # flash('Email already exists.',category='error')
       #   return jsonify({'message': 'Email already exists.'})
       return jsonify({'status':400,'message': 'Email already exists.'})
    if user2:
       # flash('Email already exists.',category='error')
       # return jsonify({'message': 'UserName already exists.'})
      return jsonify({'status':400,'message': 'UserName already exists.'})
    elif len(email) < 4:
       # flash('Email must be greater than 3 characters.',category='error')
        return jsonify({'status':400,'message': 'Email must be greater than 3 characters.'})
    elif len(user_name) <= 2:
       # flash('First name must be greater than 1 character.',category='error')
        return jsonify({'status':400,'message': 'First name must be greater than 1 character.'})
    elif password1 != password2:
       # flash('Passwords don\'t match.',category='error')
        return jsonify({'status':400,'message': 'Passwords don\'t match.'})
    elif len(password1) < 7:
       # flash('Password must be at least 7 characters.',category='error')
        return jsonify({'status':400,'message': 'Password must be at least 7 characters.'})
    else:
        new_user=User(public_id=str(uuid.uuid4()),email=email,user_name=user_name,password=generate_password_hash(
            password1,method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status':200,'message': 'user created'})

    return jsonify({'status':500,'message': 'Sql error'})


