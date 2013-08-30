from shared import db

class Athlete(db.Model):
    __tablename__ = 'athletes'


    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    coach = db.Column(db.Boolean, nullable=False)

    def is_a_coach(self):
        if self.coach:
            return 'Yes'
        else:
            return 'No'

    def __init__(self, first_name, last_name, is_coach):
        self.first_name = first_name
        self.last_name  = last_name
        self.coach = is_coach

    def __str__(self):
        return "<Athlete Name: %s %s>" % (self.first_name, self.last_name)
