from shared import db

class Class(db.Model):
    __tablename__= 'classes'

    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.Integer, nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('athletes.id'))
    coach = db.relationship('Athlete', primaryjoin='Athlete.id==Class.coach_id')

    def __init__(self, size, coach_id):
        self.size = size
        self.coach_id = coach_id

    def __str__(self):
        return "Class"
