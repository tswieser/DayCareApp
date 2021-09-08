from .db import db


class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    users = db.relationship('User', back_populates='schools')
    classes = db.relationship('Class', back_populates="schools")
    children = db.relationship('Child', back_populates="schools")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'description': self.description
        }
