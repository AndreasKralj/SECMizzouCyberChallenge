class Jurisdiction(db.Model):
  __tablename__ = 'Jurisdiction'
  patientID = db.Column(db.Integer)
  id = db.Column(db.Integer)
