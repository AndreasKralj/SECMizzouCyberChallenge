import os, json
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
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + mysqlUser + ':' + mysqlPass + '@' + mysqlHost + ':3306/' + mysqlDB
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

auth = HTTPBasicAuth()

g_Config = json.load(open('data.json'))



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
@app.route('/api/create', methods = ['POST'])
@auth.login_required
def create():
  data = request.get_json()
  if not isinstance(data['Col'], list) or not len(data['Col']):
    return False
  if not isinstance(data['Val'], list) or not len(data['Val']):
    return False
  if not isinstance(data['TableName'], str) or not len(data['TableName']):
    return False
  if not isinstance(data['Auth'], str) or not len(data['Auth']): # or not verify_token(data['Auth']):
    return False

  permissionList = g_Config['ActorRelations'][g.user.authType]["CreateAccess"]
  # If for loop exits without returning, all requested columns are in userType's permission list
  for c in data['Col']:
    if not isinstance(c, str):
      return False
    if c not in permissionList:
      return False
  # check that all values are strings
  for v in data['Val']:
    if not isinstance(c, str):
      return False

  # Make sure there is all entries are col/val pairs
  if len(data['Col']) != len(data['Val']):
      return False



@app.route('/api/read')
def read():
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