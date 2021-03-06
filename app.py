#import smtp_test2
import os, json
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from logger import log_operation

mysqlUser = os.environ.get('MYSQL_USER')
mysqlPass = os.environ.get('MYSQL_PASS')
mysqlHost = os.environ.get('MYSQL_HOST')
mysqlDB = os.environ.get('MYSQL_DB')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + mysqlUser + ':' + mysqlPass + '@' + mysqlHost + ':3306/' + mysqlDB
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

auth = HTTPBasicAuth()

g_Config = json.load(open('config.json'))

class Patient(db.Model):
  __tablename__ = 'Patient'
  ssn = db.Column(db.Integer)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  dateOfBirth = db.Column(db.String(10))
  gender = db.Column(db.String(255))
  prescriptions = db.Column(db.String(255))
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  conditions = db.Column(db.String(255))
  patientID = db.Column(db.Integer, primary_key = True)
  
  
class Jurisdiction(db.Model):
  __tablename__ = 'Jurisdiction'
  patientID = db.Column(db.Integer, primary_key = True)
  id = db.Column(db.Integer, primary_key = True)


class User(db.Model):
  __tablename__ = 'User'
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  authType = db.Column(db.String(255))
  email = db.Column(db.String(255))
  password = db.Column(db.String(255))
  id = db.Column(db.Integer, primary_key = True)
  
  def __repr__(self):
    return '<User %r>' % self.email

  # called when adding a user
  def hash_password(self, password):
    self.password = pwd_context.hash(password)

  # called to verify a user
  def verify_password(self, password):
    return pwd_context.verify(password, self.password)

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


@app.route('/api/test', methods = ['POST'])
def test():
  res = db.engine.execute("SELECT * FROM User;")
  print(type(res))
  names = []
  for row in res:
    names.append(row[0])
  print(names)
  return "True"

@app.route('/api/addUser', methods = ['POST'])
def new_user():
  username = request.json.get('email')
  password = request.json.get('password')
  if username is None or password is None:
    print(">>> user or pass empty")
    os.abort() # missing arguments
  if User.query.filter_by(email = username).first() is not None:
    print(">>> no row found")
    os.abort() # existing user
  user = User(email = username)
  user.hash_password(password)
  user.firstName = request.json.get('firstName')
  user.lastName = request.json.get('lastName')
  user.authType = request.json.get('authType')
  db.session.add(user)
  db.session.commit()
  return jsonify({ 'email': user.email }), 201, #{'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/api/getToken')
@auth.login_required
def get_auth_token():
  print(">> g.user")
  print(g.user)
  token = g.user.generate_auth_token()
  print(type(token))
  return jsonify({ 'token': token.decode('ascii') })

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
      print(">>> user was none")
      # try to authenticate with username/password
      user = User.query.filter_by(email = username_or_token).first()
      if not user or not user.verify_password(password):
        return False
    print(user)
    g.user = user
    return True


# Action routes
@app.route('/api/create', methods = ['POST'])
@auth.login_required
def create():
  data = request.get_json()
  if not isinstance(data['Col'], list) or not len(data['Col']):
    return "col"
  if not isinstance(data['Val'], list) or not len(data['Val']):
    return "val"
  if not isinstance(data['TableName'], str) or not len(data['TableName']):
    return "table"

  permissionList = g_Config['ActorRelations'][g.user.authType]["CreateAccess"]
  # If for loop exits without returning, all requested columns are in userType's permission list
  for c in data['Col']:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "col not str"
  # check that all values are strings
  for v in data['Val']:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "val not str"

  # Make sure there is all entries are col/val pairs
  if len(data['Col']) != len(data['Val']):
    return "len"

  # check requested table exists
  if data['TableName'] not in permissionList:
    logging.error('some type of tablename error')
    return "tablename invalid"

  db.engine.execute("INSERT INTO " + data['TableName'] + "(" + ",".join(data['Col']) + ') VALUES ("' + '","'.join(data['Val']) + '");')

  log_operation(g.user.id,'c',True,True)
  return "Success"



@app.route('/api/read', methods = ['POST'])
@auth.login_required
def read():
  #Get data from the JSON
  data = request.get_json()
  #First, verify that the types of the values in the dictionary are what they should be.
  if not isinstance(data["TableName"],str) or not len(data['TableName']):
    print("This is an error.")
  if not isinstance(data["SearchCol"],list) or not len(data['SearchCol']):
    print("This is an error.")
  if not isinstance(data["SearchVal"], list) or not len(data['SearchVal']):
    print("This is an error.")
  if not isinstance(data["ReqCol"], list) or not len(data['ReqCol']):
    print("This is an error.")
  if not isinstance(data["Consent"],list):
    print("This is an error.")

  #Check if search & request cols are in the read access permission
  for c in data["SearchCol"]:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "search col not str"
    try:
      colTableDict = g_Config["ActorRelations"][g.user.authType]["ReadAccess"][ data["TableName"] + "." + c ]
    except KeyError:
      log_operation(g.user.id,'r',False,True)
      return "No access or doesn't exist"

  for c in data["ReqCol"]:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "request col not str"
    try:
      colTableDict = g_Config["ActorRelations"][g.user.authType]["ReadAccess"][ data["TableName"] + "." + c ]
    except KeyError:
      log_operation(g.user.id,'r',False,True)
      return "No access or doesn't exist"

  # Make sure there is all entries are col/val pairs
  if len(data['SearchCol']) != len(data['SearchVal']):
    log_operation(g.user.id,'r',False,True)
    return "lenError"

  #construct comparison
  comp = data['SearchCol'][0] + " = " 
  if isinstance(data["SearchVal"][0], str):
    comp += "'" + data['SearchVal'][0] + "'"
  elif isinstance(data["SearchVal"][0], int):
    comp += str(data['SearchVal'][0])
  for i in range(1,len(data['SearchCol'])):
    comp += " AND " + data['SearchCol'][i] + " = " 
    if isinstance(data["SearchVal"][i], str):
      comp += "'" + data['SearchVal'][i] + "'"
    elif isinstance(data["SearchVal"][i], int):
      comp += str(data['SearchVal'][i])

  res = db.engine.execute("SELECT " + ','.join(data['ReqCol']) + " FROM " + data['TableName'] + " WHERE " + comp )
  print(type(res))
  names = []
  for row in res:
    names.append(str(row))
  print(names)

  log_operation(g.user.id,'r',True,True)
  return "Success"


@app.route('/api/update', methods = ['POST'])
@auth.login_required
def update():
  #Get data from the JSON
  data = request.get_json()

  if not isinstance(data["TableName"],str) or not len(data['TableName']):
    print("This is an error.")
  if not isinstance(data["SearchCol"],list):
    print("This is an error.")
  if not isinstance(data["SearchVal"], list):
    print("This is an error.")
  if not isinstance(data["UpdateCol"], list) or not len(data['UpdateCol']):
    print("This is an error.")
  if not isinstance(data["UpdateVal"], list) or not len(data['UpdateVal']):
    print("This is an error.")
  if not isinstance(data["Consent"],list):
    print("This is an error.")

  # Make sure there is all entries are col/val pairs
  if len(data['SearchCol']) != len(data['SearchVal']):
    log_operation(g.user.id,'r',False,True)
    return "lenError - search"
  if len(data['UpdateCol']) != len(data['UpdateVal']):
    log_operation(g.user.id,'r',False,True)
    return "lenError - update"

  #Check if search & request cols are in the read access permission
  for c in data["SearchCol"]:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "search col not str"
    try:
      colTableDict = g_Config["ActorRelations"][g.user.authType]["ModifyAccess"][ data["TableName"] + "." + c ]
    except KeyError:
      log_operation(g.user.id,'r',False,True)
      return "No access or doesn't exist"

  for c in data["UpdateCol"]:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "update col not str"
    try:
      colTableDict = g_Config["ActorRelations"][g.user.authType]["ModifyAccess"][ data["TableName"] + "." + c ]
    except KeyError:
      log_operation(g.user.id,'r',False,True)
      return "No access or doesn't exist"

  #construct update fields & values
  setList = []
  for i in range(0,len(data['UpdateCol'])):
    if isinstance(data["UpdateVal"][i], str):
      setList.append(data['UpdateCol'][i] + " = '" + data['UpdateVal'][i] + "'")
    elif isinstance(data["UpdateVal"][i], int):
      setList.append(data['UpdateCol'][i] + " = " + str(data['UpdateVal'][i]))

  if len(data["SearchCol"]):
    #construct comparison
    comp = data['SearchCol'][0] + " = "
    if isinstance(data["SearchVal"][0], str):
      comp += "'" + data['SearchVal'][0] + "'"
    elif isinstance(data["SearchVal"][0], int):
      comp += str(data['SearchVal'][0])
    for i in range(1,len(data['SearchCol'])):
      comp += " AND " + data['SearchCol'][i] + " = " 
      if isinstance(data["SearchVal"][i], str):
        comp += "'" + data['SearchVal'][i] + "'"
      elif isinstance(data["SearchVal"][i], int):
        comp += str(data['SearchVal'][i])

  db.engine.execute("UPDATE " + data['TableName'] + " SET " + ",".join(setList) + " WHERE " + comp)
  log_operation(g.user.id,'u',True,True)
  return "Success"

@app.route('/api/delete', methods=['POST'])
@auth.login_required
def delete():
  data = request.get_json()
  if not isinstance(data['SearchCol'], list) or not len(data['SearchCol']):
    return "col"
  if not isinstance(data['SearchVal'], list) or not len(data['SearchVal']):
    return "val"
  if not isinstance(data['TableName'], str) or not len(data['TableName']):
    return "table"
  if not isinstance(data['Consent'], list):
    return "consent"

  permissionList = g_Config['ActorRelations'][g.user.authType]["DeleteAccess"]
  # If for loop exits without returning, all requested columns are in userType's permission list
  for c in data['SearchCol']:
    if not isinstance(c, str):
      logging.error('SQL error was encountered')
      return "col not str"

  # Make sure there is all entries are col/val pairs
  if len(data['SearchCol']) != len(data['SearchVal']):
    return "len"

  # check requested table exists
  if data['TableName'] not in permissionList:
    logging.error('some type of tablename error')
    return "tablename invalid"

  #construct comparison
  comp = data['SearchCol'][0] + " = "
  if isinstance(data["SearchVal"][0], str):
    comp += "'" + data['SearchVal'][0] + "'"
  elif isinstance(data["SearchVal"][0], int):
    comp += str(data['SearchVal'][0])
  for i in range(1,len(data['SearchCol'])):
    comp += " AND " + data['SearchCol'][i] + " = " 
    if isinstance(data["SearchVal"][i], str):
      comp += "'" + data['SearchVal'][i] + "'"
    elif isinstance(data["SearchVal"][i], int):
      comp += str(data['SearchVal'][i])

  db.engine.execute("DELETE FROM " + data['TableName'] + " WHERE " + comp);

  log_operation(g.user.id,'d',True,True)
  return "Success"



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
