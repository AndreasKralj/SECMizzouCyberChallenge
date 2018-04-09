import app
import os
from flask_sqalchemy import SQLAlchemy
from flask_httpauth import SQLAlchemy

class User(db.Model):
  __tablename__ = 'Users'
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  authType = db.Column(db.String(255))
  email = db.Column(db.String(255))
  id = db.Column(db.Integer, primary_key = True)  
