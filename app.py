import os
#import smtp_test2
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

mysqlUser = os.environ.get('MYSQL_USER')
mysqlPass = os.environ.get('MYSQL_PASS')
mysqlHost = os.environ.get('MYSQL_HOST')
mysqlDB = os.environ.get('MYSQL_DB')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + mysqlUser + ':' + mysqlPass + '@' + mysqlHost + ':3306/' + mysqlDB
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

auth = HTTPBasicAuth()


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(32), index = True)
  password_hash = db.Column(db.String(128))
  authType = db.Column(db.String(128))

  def __repr__(self):
    return '<User %r>' % self.username

  # called when adding a user
  def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

  # called to verify a user
  def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)

  def generate_auth_token(self, expiration = 600):
    s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({ 'id': self.id })

  @staticmethod
  def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
      data = s.loads(token)
    except SignatureExpired:
      return None # valid token, but expired
    except BadSignature:
      return None # invalid token
    user = User.query.get(data['id'])
    return user


@app.route('/api/addUser', methods = ['POST'])
def new_user():
  username = request.json.get('username')
  password = request.json.get('password')
  if username is None or password is None:
    abort(400) # missing arguments
  if User.query.filter_by(username = username).first() is not None:
    abort(400) # existing user
  user = User(username = username)
  user.hash_password(password)
  db.session.add(user)
  db.session.commit()
  return jsonify({ 'username': user.username }), 201, #{'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/api/getToken')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


# Action routes
@app.route('/api/create')
def create():
  pass

@app.route('/api/read')
def read():
  #Get data from the JSON
  data=request.get_json()
  #First, verify that the types of the values in the dictionary are what they should be.
  if not isinstance(data["TableName"],str):
    #Error
    print("This is an error.")
  if not isinstance(data["SearchCol"],list):
    #Error
    print("This is an error.")
  if not isinstance(data["SearchVal"], list):
    #Error
    print("This is an error.")
  if not isinstance(data["UpdateCol"], list):
    #Error
    print("This is an error.")
  if not isinstance(data["UpdateVal"],list):
    #Error
    print("This is an error.")
  if not isinstance(data["Auth"],str):
    #Error
    print("This is an error.")
  if not isinstance(data["Consent"],list):
    #Error
    print("This is an error.")
        
  #Part 2: Verify the authentication.

  #Check if the user is in the read access permission settings. Check the range of the list to see if the user is in the _ColTableIdentifier list.
  for i in range(0,len(data["ActorRelations"]["_ActorType"]["ReadAccess"]["_ColTableIdentifier"])):
    #This username is taken from the table that has the user's info in it.
    if data["ActorRelations"]["_ActorType"]["ReadAccess"]["_ColTableIdentifier"] == username:
      #This means a match occurred. Check if the number of consentors required for this action is greater than 0. If it is greater than 0, notify the actors.
      for i in range(0, len(data["ActorRelations"]["_ActorType"]["ReadAccess"]["_ColTableIdentifier"]["ReqConsentors"])):
        if data["ActorRelations"]["_ActorType"]["ReadAccess"]["_ColTableIdentifier"]["ReqConsentors"][i] >= 0:
        #Notify the required consentors. Check their access levels to confirm whether the names set in the file are correct.
        #Check access levels
            print("Checking access levels")
        #Notify
        if SendSSLEmail(email, message) == 0:
          print("Success!");
        else:
          print("Failure");
        
        

    
  #Part 3: Query the table via the userid from the auth.
  

  pass

@app.route('/api/update')
def update():
  pass

@app.route('/api/delete')
def delete():
  pass



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)