class Patients(db.Model):
  __tablename__ = 'Patients'
  ssn = db.Column(db.Integer)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  dateOfBirth = db.Column(db.String(10))
  gender = db.Column(db.String(255))
  prescriptions = db.Column(db.String(255))
  height = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  conditions = db.Column(db.String(255))
  patientID = db.Column(db.Integer)
  
