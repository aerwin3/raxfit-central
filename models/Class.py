from mongoalchemy.document import Document, Index
from mongoalchemy.fields import StringField,IntField

class Class(Document):

    time = StringField()
    coach = StringField()
    size = IntField(min_value=0, required=True)

    def __repr__(self):
        return super(Class, self).__repr__()

