from shared import db

class Class(db.Model):
    __tablename__= 'classes'

    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.Integer, nullable=False)
    wod = db.Column(db.Text)

    type_id = db.Column(db.Integer, db.ForeignKey('class_types.id'))

    sessions = db.relationship('ClassSession', backref='classes', lazy='dynamic')
    type = db.relationship("ClassType", primaryjoin='ClassType.id==Class.type_id')

    def __init__(self, size, wod, type_id):
        self.size = size
        self.type_id = type_id
        self.wod = wod

    def __str__(self):
        return "Class"

class ClassType(db.Model):
    __tablename__ = "class_types"

    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.String)

    def __init__(self, value):
        self.value = value

class ClassSession(db.Model):
    __tablename__ = "class_sessions"

    id = db.Column(db.Integer, primary_key = True)
    class_id = db.Column(db.Integer,db.ForeignKey('classes.id'))
    dateTime = db.Column(db.Date, nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('athletes.id'))
    coach = db.relationship('Athlete', primaryjoin='Athlete.id==ClassSession.coach_id')

    def __init__(self, dateTime, coach_id):
        self.coach_id = coach_id
        self.dateTime = dateTime