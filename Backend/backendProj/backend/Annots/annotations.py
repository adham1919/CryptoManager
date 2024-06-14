from functools import wraps
from flask import request,jsonify,current_app as app
from backend.Models.User import User
import jwt
from backend import blacklist



def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None

        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        print(token)
        if not token:
            return jsonify({'status':401,'message': 'Token is missing!'}),401
        if token in blacklist:
            return jsonify({'status':401,'message': 'Token is Logged out!'}),401
        try:
            print('sss')
            data=jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
            print('eee')
            current_user=User.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            print(e)
            return jsonify({'status':401,'message': 'Token is invalid!'}),401

        return f(current_user,*args,**kwargs)

    return decorated
